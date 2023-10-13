from library.srap_data_routeur import scrap_datas


def main():
    url = "https://books.toscrape.com/index.html"
    url_two = "https://books.toscrape.com/catalogue/the-mysterious-affair-at-styles-hercule-poirot-1_452/index.html"
    url_three = "https://books.toscrape.com/catalogue/misery_334/index.html"
    category_url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

    # pass the home page url
    scrap_datas(url)

    # pass a book url
    # scrap_datas(url_two)

    # pass a false url
    # scrap_datas(url_three)

    # pass a category url
    # scrap_datas(category_url)


if __name__ == '__main__':
    main()
