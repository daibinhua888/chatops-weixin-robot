import json


def load_config(file_path):
    file = open(file_path, 'r')
    txt = file.read()
    return json.loads(txt)
