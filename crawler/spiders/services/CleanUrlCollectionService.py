import validators as _validators
import requests as _requests

def clean_url_collection(urls: list[str]) -> list[str]:
    urls = list(set(urls))
    cleaned_urls = list()
    for url in urls:
        if _validators.url(url):
            response = _requests.get(url)
            if response.status_code >= 200 and response.status_code < 300:
                cleaned_urls.append(url)
    return cleaned_urls