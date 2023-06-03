import json
import yaml


def parse_json(filepath):
    try:
        return json.load(open(filepath, mode="r"))
    except FileNotFoundError:
        return "file_not_found"


def parse_yaml(filepath):
    try:
        return yaml.safe_load(open(filepath, mode="r"))
    except FileNotFoundError:
        return "file_not_found"


def parse_file(filepath):
    if filepath.endswith(".json"):
        return parse_json(filepath)
    elif filepath.endswith(".yaml") or filepath.endswith(".yml"):
        return parse_yaml(filepath)
    else:
        return "file_format_error"
