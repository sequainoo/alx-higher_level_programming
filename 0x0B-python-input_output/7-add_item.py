#!/usr/bin/python3
"""Adds all arguments to a list and save them to file as json.
"""


import sys


def main():
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file =  __import__('6-load_from_json_file').load_from_json_file
    filename = 'add_item.json'

    l = [sys.argv[i] for i in range(1, len(sys.argv))]
    try:
        existing_content = load_from_json_file(filename)
    except:
        existing_content = []
    content = existing_content + l
    save_to_json_file(content, filename)

main()
