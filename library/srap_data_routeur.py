from library.scrap_category import scrap_all_category_books
from library.scrap_book_function import get_book_data
from library.http_functions import url_type, check_url
import requests


def scrap_datas(url):
    url_page = requests.get(url)

    # if the url exist, check it's the home, a category or a book's page then call the right function
    if check_url(url_page):
        type_of_url = url_type(url)
        if type_of_url == "home":
            print("Welcome home")
        elif type_of_url == "category":
            scrap_all_category_books(url)
        else:
            get_book_data(url)

