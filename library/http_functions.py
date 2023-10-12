
def check_url(url) -> bool:
    is_url_exist = url.status_code == 200

    if is_url_exist:
        print("This url is valid")
    else:
        print("ERROR 404 -> This page doesn't exist")

    return is_url_exist
