from crawler.models import Bus, Image
from crawler.spiders.services.CleanUrlCollectionService import clean_url_collection
from crawler.spiders.services.GetPageService import bs4_get_page
from django.db import transaction
from typing import List
from urllib.parse import urljoin

def scrap() -> None:
    base_url = "http://absolutebus.com/"
    source_url="http://absolutebus.com/listings/"
    page = bs4_get_page(source_url)
    urls = page.select_one('#bodytext').find_all('a', href=True)
    urls = list(set(urls))
    cleaned_urls = list()
    for url in urls:
        cleaned_urls.append(base_url + url['href'][3:])
    cleaned_urls = clean_url_collection(cleaned_urls)
    buses = list()
    for url in cleaned_urls:
        bus = Bus(source_url=url)
        bus = get_bus_info(bus)
        buses.append(bus)

# This is going to be always pretty similar, just change the selectors. Sometimes we need to treat the data, and it can be done here using different services.
def get_bus_info(bus: Bus) -> Bus:
    page = bs4_get_page(bus.source_url)
    try:
        with transaction.atomic():
            bus.title = page.select_one('#headertext').find_all('h2')[0].text.strip()
            bus.price = page.select_one('#bodytext').find_all('h3')[0].text.strip()
            bus.save()

            images = page.select_one('#bodytext').find_all('img')
            image_objects: List[Image] = []
            for image in images:
                src_ = urljoin(bus.source_url, image['src'])
                image_objects.append(Image(bus=bus, url=src_))
            Image.objects.bulk_create(image_objects)
    except:
        pass
    return bus