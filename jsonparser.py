import json
from typing import List, Union

from model import Entry


def build_model(file_name: str) -> Entry:
    entry = Entry(file_name)

    with open(file_name, "r") as f:
        json_data = json.load(f)

    entry.children = convert_json(json_data)

    return entry


def convert_json(json_data: Union[dict, list, str, int]) -> List[Entry]:
    if isinstance(json_data, (str, int)):
        return []

    entries: List[Entry] = []

    if isinstance(json_data, list):
        for entry in json_data:
            entries.extend(convert_json(entry))
    elif isinstance(json_data, dict):
        for (name, value) in json_data.items():
            name = str(name)

            if isinstance(value, list):
                entry = Entry(name)
                for child in value:
                    entry.children.extend(convert_json(child))
            elif isinstance(value, (str, int)):
                entry = Entry(name)  # no children
            elif isinstance(value, dict):
                children = convert_json(value)
                entry = Entry(name, children)
            else:
                raise AssertionError(f"value of type {str(type(value))} could not be processed")

            entries.append(entry)

    return entries
