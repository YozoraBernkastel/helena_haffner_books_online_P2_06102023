import os
import urllib.request
from os import path, stat
import csv


def book_data_export(data_dict: dict):
    if not path.exists("outputs/csv/"):
        os.makedirs("outputs/csv/")

    file_path = "outputs/csv/" + data_dict["Category"] + "_export.csv"
    # if the file doesn't exist or if it is empty, write the header by using the keys from data_dict
    if not path.exists(file_path) or stat(file_path).st_size == 0:
        with open(file_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow((data_dict.keys()))

    # export data if there is data in the dictionary
    if len(data_dict) > 0:
        with open(file_path, 'a') as d:
            writer = csv.writer(d)
            writer.writerow((data_dict.values()))

        print("export " + data_dict["Title"] + " data with success !")

    else:
        print("There is no Data to export.")


def save_cover(upc, category, url):
    if not path.exists("outputs/img/" + category + "/"):
        os.makedirs("outputs/img/" + category + "/")

    file_path = "outputs/img/" + category + "/" + upc + url[77:]
    urllib.request.urlretrieve(url, file_path)
