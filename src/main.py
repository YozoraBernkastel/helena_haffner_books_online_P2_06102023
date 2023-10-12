from library.scrap_functions import *


def main():

    #  will need to create a prompt which will ask for an url the pass it in get_book_data function
    url = "https://books.toscrape.com/catalogue/the-mysterious-affair-at-styles-hercule-poirot-1_452/index.html"
    url_two = "https://books.toscrape.com/catalogue/misery_334/index.html"
    url_three = "https://books.toscrape.com/catalogue/misery_332/index.html"
    get_book_data(url)
    get_book_data(url_two)
    get_book_data(url_three)


if __name__ == '__main__':
    main()

