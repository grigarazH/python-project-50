import json
import yaml


def get_file_format(file_content):
    if file_content.name.endswith(".json"):
        return "json"
    elif (file_content.name.endswith(".yaml")
          or file_content.name.endswith(".yml")):
        return "yaml"
    else:
        raise ValueError('wrong_file_format')


def parse_file(file_content, format):
    if format == "json":
        return json.load(file_content)
    else:
        return yaml.safe_load(file_content)
