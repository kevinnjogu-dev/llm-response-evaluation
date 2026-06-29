import json


def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(data, filepath):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)