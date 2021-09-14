import csv
from collections import defaultdict
from itertools import islice, zip_longest


def flatten_dict(data):
    """Merges similar keys of a list of dicts"""
    dd = defaultdict(list)
    for d in data:
        for key, value in d["main"].items():
            dd[key].append(value)
    return dd


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


def write_to_csv(csvfile, header, data):
    with open(csvfile.lower(), "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(header)
        csv_writer.writerows(data)


def write_json_to_csv(jsondata, csvfile=""):
    """Writes JSON data to CSV file"""
    data_to_write = flatten_dict(jsondata["list"])
    csv_header = data_to_write.keys()
    csv_data = zip_longest(*data_to_write.values(), fillvalue="")
    write_to_csv(csvfile, csv_header, csv_data)


def generate_report(expected="", actual="", output="", limit_columns=None):
    """
    Reads "limit_columns" number of columns from expected and actual CSVs.
    Then writes data to output CSV by placing similar rows side by side
    """
    with open(expected) as f1, open(actual) as f2:
        e_csv = csv.reader(f1)
        a_csv = csv.reader(f2)
        e_csv_header = take(
            limit_columns, map(lambda key: f"Expected {key.title()}", next(e_csv))
        )
        a_csv_header = take(
            limit_columns, map(lambda key: f"Actual {key.title()}", next(a_csv))
        )
        header = [val for pair in zip(e_csv_header, a_csv_header) for val in pair]
        data = list()
        for e_row, a_row in zip(e_csv, a_csv):
            data_e_row = take(limit_columns, e_row)
            data_a_row = take(limit_columns, a_row)
            data.append([val for pair in zip(data_e_row, data_a_row) for val in pair])
        write_to_csv(output, header, data)
