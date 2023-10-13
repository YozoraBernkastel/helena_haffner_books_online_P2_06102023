from library.scrap_all import scrap_all
from library.scrap_category import scrap_all_category_books
from library.scrap_book_function import get_book_data
from library.http_functions import url_type, check_url
import requests


def scrap_datas(url):
    url_page = requests.get(url)

    # if the url exist, check it's the home, a category or a book's page then call the right function
    if check_url(url_page):
        match url_type(url):
            case"home":
                scrap_all(url)
            case "category":
                scrap_all_category_books(url)
            case _:
                get_book_data(url)

    else:
        print("ERROR 404 -> This page doesn't exist !")

