from library.http_functions import check_url
from bs4 import BeautifulSoup
import requests


def get_book_data(url):
    url_page = requests.get(url)
    is_valid_url = check_url(url_page)

    if is_valid_url is False:
        return

    # in another function, with will call this one and will check the validity of the url -> check the page -> if page
    # of a book, scrap datas, if page of a category, scrap all the books' name on
    # all pages from this category then loop on those title to scrap the info of each book of this category.
    # if the page is the main page, then scrap all the categories, then loop on each to do the upper command.
    # during the scrap of a book's information, write it in the csv.
    book_data = {"product_page_url": url}

    soup = BeautifulSoup(url_page.text, 'html5lib')
    book_data["universal_product_code"] = soup.find('td').text
    book_data["title"] = soup.find('h1').text
    # à la place du return, on appellera la fonction d'export
    return book_data
