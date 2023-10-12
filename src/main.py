from library.srap_data_routeur import scrap_datas


def main():
    url = "https://books.toscrape.com/index.html"
    url_two = "https://books.toscrape.com/catalogue/misery_334/index.html"
    url_three = "https://books.toscrape.com/catalogue/misery_332/index.html"
    category_url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

    # home url
    scrap_datas(url)

    # book url
    scrap_datas(url_three)

    # false url
    scrap_datas(url_two)

    # category url
    scrap_datas(category_url)


if __name__ == '__main__':
    main()
