from gendiff.parser import parse_file


def get_diff_dict(dict1, dict2):
    diff_dict = {}
    for key, value1 in dict1.items():
        value2 = dict2.get(key)
        diff_dict[key] = {}
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff_dict[key]["children"] = get_diff_dict(value1, value2)
        elif value1 != value2:
            diff_dict[key]["removed"] = value1
        else:
            diff_dict[key]["unchanged"] = value1
    for key, value2 in dict2.items():
        value1 = dict1.get(key)
        if not diff_dict.get(key):
            diff_dict[key] = {}
        if value1 != value2 and not (isinstance(value1, dict) and isinstance(value2, dict)):
            diff_dict[key]["added"] = value2
    return {key: value for key, value in sorted(diff_dict.items())}


def dict_to_str(dct, depth=0):
    result = "{\n"
    for key, value in dct.items():
        result += "    " * (depth + 1)
        result += format_value_stylish(key, value, depth)
        result += "\n"
    result += "    " * depth + "}"
    return result


def format_value_stylish(key, value, depth=0):
    if isinstance(value, dict):
        return f"{key}: {dict_to_str(value, depth + 1)}"
    elif isinstance(value, bool):
        return f"{key}: {str(value).lower()}"
    elif value is None:
        return f"{key}: null"
    elif value == "":
        return f"{key}:"
    else:
        return f"{key}: {value}"



def generate_diff_stylish(diff_dict, depth=0):
    result = "{\n"
    for key, _ in diff_dict.items():
        removed = diff_dict[key].get("removed")
        added = diff_dict[key].get("added")
        unchanged = diff_dict[key].get("unchanged")
        children = diff_dict[key].get("children")
        if "removed" in diff_dict[key]:
            result += "    " * depth + f"  - "
            result += format_value_stylish(key, removed, depth)
            result += "\n"
        if "added" in diff_dict[key]:
            result += "    " * depth + f"  + "
            result += format_value_stylish(key, added, depth)
            result += "\n"
        if "unchanged" in diff_dict[key]:
            result += "    " * depth + f"    "
            result += format_value_stylish(key, unchanged, depth)
            result += "\n"
        if "children" in diff_dict[key]:
            result += "    " * depth + f"    {key}: "
            result += generate_diff_stylish(children, depth + 1)
            result += "\n"
    result += "    " * depth + "}"
    return result


def generate_diff(file_path1, file_path2, formatter="stylish"):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)
    if not (file1 and file2):
        return "Wrong format"
    dict_diff = get_diff_dict(file1, file2)
    if formatter == "stylish":
        return generate_diff_stylish(dict_diff)
