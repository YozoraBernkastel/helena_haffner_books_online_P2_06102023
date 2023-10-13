from export_library.book_data_export import book_data_export
from library.http_functions import check_url
from bs4 import BeautifulSoup
import requests
import re


def get_book_data(url):
    url_page = requests.get(url)
    # in case the function is directly call by the user
    if check_url(url_page):
        book_data = {"Product_page_url": url}

        soup = BeautifulSoup(url_page.text, 'html5lib')

        # create an array containing all the td in the class "table table-striped" table ...
        table_striped_table = soup.find("table", class_="table table-striped")
        td_table = table_striped_table.find_all('td')

        # then push each needed element in a dictionary in the right order.
        book_data["Universal_product_code"] = td_table[0].text
        book_data["Title"] = soup.find('h1').text
        book_data["Price_including_tax"] = td_table[3].text[1:]
        book_data["Price_excluding_tax"] = td_table[2].text[1:]

        # scrap the number only
        book_data["Number_available"] = re.findall('[0-9]+', td_table[5].text)

        # scrap the description of the book in the metadata -> possibility to scrap it in the <article> tag with
        # the class product_page too.
        book_data["Product_description"] = soup.find("meta", attrs={"name": "description"})["content"].strip()

        # scrap the category which is in the <ul> tag with the class breadcrumb.
        breadcrumb_class_table = soup.find("ul", class_="breadcrumb")
        book_data["Category"] = breadcrumb_class_table.find_all("a")[2].text

        book_data["Review_rating"] = td_table[6].text

        # scrap the cover image's url
        img_url = soup.find("img")["src"]
        book_data["Image_URL"] = "https://books.toscrape.com" + img_url[5:]
        # Call for the export function
        book_data_export(book_data)


