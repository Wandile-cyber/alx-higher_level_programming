#!/usr/bin/python3
"""
Python function that add arguments to a Python list
"""
import sys
import os

save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
json_list = []

if os.path.exists(filename):
    json_list = load_from_json_file(filename)

for index in argv[1:]:
    json_list.append(index)

save_to_json_file(json_list, filename)
