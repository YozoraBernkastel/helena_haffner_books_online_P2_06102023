from os import path, stat
import csv


def book_data_export(data_dict: dict):
    file_path = "../outputs/data_export.csv"
    # if the file doesn't exist or if it is empty, write the header by using the keys from data_dict
    if path.exists(file_path) is False or stat(file_path).st_size == 0:
        with open(file_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow((data_dict.keys()))

    # export data
    with open(file_path, 'a') as d:
        writer = csv.writer(d)
        writer.writerow((data_dict.values()))

    print("export book's information with success !")
