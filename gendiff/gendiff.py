import json


def format_bool(value):
    return str(value).lower() if isinstance(value, bool) else value


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    file_diff = {key: (value, file2.get(key)) for key, value in file1.items()}
    for key, value in file2.items():
        file_diff[key] = file1.get(key), value
    result = "{\n"
    for key, value in sorted(file_diff.items()):
        value1_formatted = format_bool(value[0])
        value2_formatted = format_bool(value[1])
        if value[0] != value[1]:
            if value[0] is not None:
                result += f"  - {key}: {value1_formatted}\n"
            if value[1] is not None:
                result += f"  + {key}: {value2_formatted}\n"
        else:
            result += f"    {key}: {value1_formatted}\n"
    result += "}"
    return result
