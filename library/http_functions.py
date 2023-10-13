from bs4 import BeautifulSoup
import requests


def check_url(url) -> bool:
    #  todo HHA -> need to check if the url corresponding to the site
    return url.status_code == 200


def url_type(url):
    if url == "https://books.toscrape.com/index.html":
        return "home"
    else:
        soup = BeautifulSoup(requests.get(url).text, 'html5lib')
        if soup.find("ul", class_="nav nav-list"):
            return "category"
        else:
            return "book"
