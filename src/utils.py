"""
Utility functions for loading LLM evaluation data.
"""

import json


def load_json(filepath):
    """
    Load a JSON file.
    """

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(data, filepath):
    """
    Save data to JSON.
    """

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    print("Utility module loaded successfully.")