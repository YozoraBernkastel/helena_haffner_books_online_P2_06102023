
def check_url(url) -> bool:
    is_url_exist = url.status_code == 200

    if is_url_exist:
        print("This url is valid")
    else:
        print("This url is not valid")

    return is_url_exist
