from gendiff.parser import parse_file
from gendiff.formats.stylish import generate_diff_stylish
from gendiff.formats.plain import generate_diff_plain


def get_value_diff(value1, value2):
    value_diff = {}
    if isinstance(value1, dict) and isinstance(value2, dict):
        value_diff["children"] = get_diff_dict(value1, value2)
    elif value1 != value2:
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
        if not diff_dict.get(key):
            diff_dict[key] = {}
        if (value1 != value2 and not
           (isinstance(value1, dict) and isinstance(value2, dict))):
            diff_dict[key]["added"] = value2
    return {key: value for key, value in sorted(diff_dict.items())}


def generate_diff(file_path1, file_path2, format="stylish"):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)
    if not (file1 and file2):
        return "Wrong file format"
    dict_diff = get_diff_dict(file1, file2)
    if format == "stylish":
        return generate_diff_stylish(dict_diff)
    elif format == "plain":
        return generate_diff_plain(dict_diff)
    else:
        return "Wrong display format"
