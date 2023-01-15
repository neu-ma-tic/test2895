#Credit function write_json to GeeksforGeeks
#https://www.geeksforgeeks.org/append-to-json-file-using-python/

from json import load, dump

def open_jfile(filename):
    with open(filename, mode = 'r', encoding = 'utf8') as jfile_settings:
        jdata = load(jfile_settings)
        return jdata

def write_json(data, filename, indent = None):
    with open(filename, 'w') as jfile_settings:
        dump(data, jfile_settings, indent = indent)