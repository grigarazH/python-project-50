import json


def format_bool(value):
    return str(value).lower() if isinstance(value, bool) else value


def get_no_diff_string(key, value):
    return f"    {key}: {value}\n"


def get_diff_string(key, value1, value2):
    result = ""
    if value1 is not None:
        result += f"  - {key}: {value1}\n"
    if value2 is not None:
        result += f"  + {key}: {value2}\n"
    return result


def get_value_diff(key, value1, value2):
    value1_formatted = format_bool(value1)
    value2_formatted = format_bool(value2)
    result = ""
    if value1 != value2:
        result += get_diff_string(key, value1_formatted, value2_formatted)
    else:
        result += get_no_diff_string(key, value1_formatted)
    return result


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    file_diff = {key: (value, file2.get(key)) for key, value in file1.items()}
    for key, value in file2.items():
        file_diff[key] = file1.get(key), value
    result = "{\n"
    for key, value in sorted(file_diff.items()):
        result += get_value_diff(key, value[0], value[1])
    result += "}"
    return result
