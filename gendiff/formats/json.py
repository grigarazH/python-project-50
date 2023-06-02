import json


def generate_diff_json(diff_dict):
    return json.dumps(diff_dict, indent=4)
