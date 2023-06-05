import json
import yaml


def parse_file(file_content):
    try:
        if file_content.name.endswith(".json"):
            return json.load(file_content)
        elif (file_content.name.endswith(".yaml")
              or file_content.name.endswith(".yml")):
            return yaml.safe_load(file_content)
        else:
            raise ValueError('Wrong file format')
    except FileNotFoundError or json.JSONDecodeError or yaml.YAMLError:
        raise
