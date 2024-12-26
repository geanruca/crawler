from src.Models.Bus import Bus
from src.Services.CleanUrlCollectionService import clean_url_collection
from src.Services.GetPageService import bs4_get_page

def get_index_urls() -> list[Bus]:
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
    return buses

# This is going to be always pretty similar, just change the selectors. Sometimes we need to treat the data, and it can be done here using different services.
def get_bus_info(bus: Bus) -> Bus:
    page = bs4_get_page(bus.source_url)
    try:
        bus.title = page.select_one('#headertext').find_all('h2')[0].text
        bus.price = page.select_one('#bodytext').find_all('h3')[0].text
        bus.image_url = page.select_one('#bodytext').find_all('img')[0]['src']
    except:
        pass
    print(bus)
    return bus