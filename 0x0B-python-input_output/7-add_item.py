#!/usr/bin/python3
"""Contains the function save_to_json_file."""


from sys import argv
import json
from pathlib import Path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

data_from_json_file = []
filename = "add_item.json"
if len(argv) == 1 and (not Path(filename).exists()):
    save_to_json_file(data_from_json_file, filename)
if len(argv) > 1:
    data_from_json_file = load_from_json_file(filename)
    for i in range(1, len(argv)):
        data_from_json_file.append(argv[i])
    save_to_json_file(data_from_json_file, filename)
