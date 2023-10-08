from library.scrap_functions import *


def main():
    url = "https://books.toscrape.com/catalogue/the-mysterious-affair-at-styles-hercule-poirot-1_452/index.html"
    print(get_book_data(url))


if __name__ == '__main__':
    main()

