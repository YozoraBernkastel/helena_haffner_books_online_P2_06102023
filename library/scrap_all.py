from library.scrap_category import scrap_all_category_books
from library.http_functions import check_url
from bs4 import BeautifulSoup
import requests


def scrap_all(url):
    url_page = requests.get(url)

    # in case the function is directly call by the user
    if check_url(url_page):
        soup = BeautifulSoup(url_page.text, 'html5lib')
        nav = soup.find("div", class_="side_categories")
        nav_li = nav.find_all("li")
        for category in nav_li:
            category_name = category.find("a").text
            category_url = category.find("a")["href"]
            # Don't scrap this category because it contains all books.
            # The other possibility is to scrap this category only.
            if category_url != "catalogue/category/books_1/index.html":
                print(category_name)
                scrap_all_category_books("https://books.toscrape.com/" + category_url)
