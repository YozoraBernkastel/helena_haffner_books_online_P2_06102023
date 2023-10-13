from library.scrap_book_function import get_book_data
from library.http_functions import check_url
from bs4 import BeautifulSoup
import requests


def scrap_all_category_books(url):
    url_page = requests.get(url)

    while check_url(url_page):
        soup = BeautifulSoup(url_page.text, 'html5lib')
        library = soup.find_all("article", class_="product_pod")
        for book in library:
            book_url = book.find("a")["href"]
            get_book_data("https://books.toscrape.com/catalogue/" + book_url[9:])

        link_to_next = soup.find("li", class_="next")
        if link_to_next:
            next_page_url = url[:-10] + link_to_next.find("a")["href"]
            print(next_page_url)
            url_page = requests.get(next_page_url)
        else:
            break
