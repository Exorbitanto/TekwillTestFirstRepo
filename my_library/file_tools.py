import json


def get_list_from_json_file(file_name):
    try:
        file = open(file_name, 'r')
        text = file.read()
        file.close()
        try:
            return json.loads(text)
        except Exception:
            return list()
    except FileNotFoundError:
        file = open(file_name, 'w+')
        file.close()