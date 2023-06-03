from gendiff.parser import parse_file
from gendiff.formats.stylish import generate_diff_stylish
from gendiff.formats.plain import generate_diff_plain
from gendiff.formats.json import generate_diff_json


def get_value_diff(value1, value2):
    value_diff = {}
    if isinstance(value1, dict) and isinstance(value2, dict):
        value_diff["type"] = "dict"
        value_diff["children"] = get_diff_dict(value1, value2)
    else:
        value_diff["type"] = "value"
        if value1 != value2:
            value_diff["removed"] = value1
        else:
            value_diff["unchanged"] = value1
    return value_diff


def get_diff_dict(dict1, dict2):
    diff_dict = {}
    for key, value1 in dict1.items():
        value2 = dict2.get(key)
        diff_dict[key] = get_value_diff(value1, value2)
    for key, value2 in dict2.items():
        value1 = dict1.get(key)
        if key not in diff_dict:
            diff_dict[key] = {"type": "value"}
        if (value1 != value2 and not
           (isinstance(value1, dict) and isinstance(value2, dict))):
            diff_dict[key]["added"] = value2
    return {key: value for key, value in sorted(diff_dict.items())}


def format_diff(dict_diff, format):
    if format == "stylish":
        return generate_diff_stylish(dict_diff)
    elif format == "plain":
        return generate_diff_plain(dict_diff)
    elif format == "json":
        return generate_diff_json(dict_diff)
    else:
        return "Wrong display format"


def generate_diff(file_path1, file_path2, format="stylish"):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)
    if (isinstance(file1, FileNotFoundError) or isinstance(file2,
                                                           FileNotFoundError)):
        return "Files not found"
    if not (file1 and file2):
        return "Wrong file format"
    dict_diff = get_diff_dict(file1, file2)
    return format_diff(dict_diff, format)
