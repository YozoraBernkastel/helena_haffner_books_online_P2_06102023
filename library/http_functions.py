from bs4 import BeautifulSoup
import requests


def check_url(url) -> bool:
    is_url_exist = url.status_code == 200
    return is_url_exist


def url_type(url):
    if url == "https://books.toscrape.com/index.html":
        return "home"
    else:
        soup = BeautifulSoup(requests.get(url).text, 'html5lib')
        if soup.find("ul", class_="nav nav-list"):
            return "category"
        else:
            return "book"
