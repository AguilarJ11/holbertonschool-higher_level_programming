#!/usr/bin/python3

"""
Convert a CSV file to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_file):
    """
    Convert a CSV file to JSON format.

    Args:
        csv_file (str): Path to the CSV file to be converted.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    data = []

    try:
        with open(csv_file, encoding='utf-8') as csvf:
            csv_reader = csv.DictReader(csvf)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        return False
    
    with open("data.json", "w", encoding="utf-8") as jf:
        json.dump(data, jf)

    return True
