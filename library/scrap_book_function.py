from library.http_functions import check_url
from bs4 import BeautifulSoup
from export_library.book_data_export import book_data_export
import requests
import re


def get_book_data(url):
    url_page = requests.get(url)

    if check_url(url_page) is True:
        # !!!! TEMPORARY COMMENT  -> in another function, with will call this one and will check the validity of the url ->
        # check the page -> if page of a book, scrap datas, if page of a category, scrap all the books' name on
        # all pages from this category then loop on those title to scrap the info of each book of this category.
        # if the page is the main page, then scrap all the categories, then loop on each to do the upper command.
        # during the scrap of a book's information, write it in the csv.
        book_data = {"product_page_url": url}

        soup = BeautifulSoup(url_page.text, 'html5lib')

        # create an array containing all the td in the class "table table-striped" table ...
        table_striped_table = soup.find("table", class_="table table-striped")
        td_table = table_striped_table.find_all('td')

        # then push each needed element in a dictionary in the right order.
        book_data["universal_product_code"] = td_table[0].text
        book_data["title"] = soup.find('h1').text
        book_data["price_including_tax"] = td_table[3].text
        book_data["price_excluding_tax"] = td_table[2].text

        # scrap the number only
        book_data["number_available"] = re.findall('[0-9]+', td_table[5].text)

        # scrap the description of the book in the metadata -> possibility to scrap it in the <article> tag with
        # the class product_page too.
        book_data["product_description"] = soup.find("meta", attrs={"name": "description"})["content"].strip()

        # scrap the category which is in the <ul> tag with the class breadcrumb.
        breadcrumb_class_table = soup.find("ul", class_="breadcrumb")
        book_data["category"] = breadcrumb_class_table.find_all("a")[2].text

        book_data["review_rating"] = td_table[6].text

        # Call for the export function
        book_data_export(book_data)

    else:
        print("ERROR 404 -> This page doesn't exist")
