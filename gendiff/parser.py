import json
import yaml


def parse_json(filepath):
    return json.load(open(filepath, mode="r"))


def parse_yaml(filepath):
    return yaml.safe_load(open(filepath, mode="r"))


def parse_file(filepath):
    if filepath.endswith(".json"):
        return parse_json(filepath)
    elif filepath.endswith(".yaml") or filepath.endswith(".yml"):
        return parse_yaml(filepath)
    else:
        return False

