from library.scrap_book_function import *
from library.scrap_category import scrap_all_category_books


def main():
    # url = "https://books.toscrape.com/catalogue/the-mysterious-affair-at-styles-hercule-poirot-1_452/index.html"
    # url_two = "https://books.toscrape.com/catalogue/misery_334/index.html"
    # url_three = "https://books.toscrape.com/catalogue/misery_332/index.html"
    # get_book_data(url)
    # get_book_data(url_two)
    # get_book_data(url_three)
    category_url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    scrap_all_category_books(category_url)


if __name__ == '__main__':
    main()

