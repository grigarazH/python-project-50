from gendiff.parser import parse_file
from gendiff.formats.stylish import generate_diff_stylish
from gendiff.formats.plain import generate_diff_plain
from gendiff.formats.json import generate_diff_json


def get_value_diff(value1, value2):
    value_diff = {}
    if isinstance(value1, dict) and isinstance(value2, dict):
        value_diff["children"] = get_diff_dict(value1, value2)
    else:
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
            diff_dict[key] = {}
        if (value1 != value2 and not
           (isinstance(value1, dict) and isinstance(value2, dict))):
            diff_dict[key]["added"] = value2
    return {key: value for key, value in sorted(diff_dict.items())}


def format_diff(diff_dict, format):
    if format == "stylish":
        return generate_diff_stylish(diff_dict)
    elif format == "plain":
        return generate_diff_plain(diff_dict)
    elif format == "json":
        return generate_diff_json(diff_dict)
    else:
        return "Wrong display format"


def generate_diff(file_path1, file_path2, format="stylish"):
    file1_content = parse_file(file_path1)
    file2_content = parse_file(file_path2)
    if file1_content == "file_not_found" or file2_content == "file_not_found":
        return "Files not found"
    if (file1_content == "file_format_error"
       or file2_content == "file_format_error"):
        return "Wrong file format"
    diff_dict = get_diff_dict(file1_content, file2_content)
    return format_diff(diff_dict, format)
