"""Adds all arguments to a list and save them to file as json.
"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def main(l=[]):
    filename = 'add_item.json'
    existing_content = load_from_json_file(filename)
    content = existing_content + l
    save_to_json_file(content, filename)

if __name__ == '__main__':
    l = [sys.argv[i] for i in range(1, len(sys.argv))]
    main(l)
