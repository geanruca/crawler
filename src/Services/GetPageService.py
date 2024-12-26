import bs4 as _bs4
import requests as _requests

def bs4_get_page(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url, verify=False)
    return _bs4.BeautifulSoup(page.content, "html.parser")