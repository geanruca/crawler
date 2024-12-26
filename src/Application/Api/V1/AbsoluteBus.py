import bs4 as _bs4
import requests as _requests

from src.Domain.Models.Bus import Bus


# This should be a service
def _get_page(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url, verify=False)
    return _bs4.BeautifulSoup(page.content, "html.parser")


def get_index_urls() -> list[Bus]:
    base_url = "http://absolutebus.com/"
    source_url="http://absolutebus.com/listings/"
    page = _get_page(source_url)
    urls = page.select_one('#bodytext').find_all('a', href=True)
    urls = list(set(urls))
    for url in urls:
        url = base_url + url['href'][3:]
        print(url)
    urls = validators.url(urls)
    buses = list()
    for url in urls:
        buses.append(Bus(source_url=url['href']))
    return buses

