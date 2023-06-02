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


def generate_value_diff_stylish(key, value_diff, depth=0):
    result = ""
    removed = value_diff.get("removed")
    added = value_diff.get("added")
    unchanged = value_diff.get("unchanged")
    children = value_diff.get("children")
    if "removed" in value_diff:
        result += "    " * depth + "  - "
        result += format_value_stylish(key, removed, depth)
        result += "\n"
    if "added" in value_diff:
        result += "    " * depth + "  + "
        result += format_value_stylish(key, added, depth)
        result += "\n"
    if "unchanged" in value_diff:
        result += "    " * depth + "    "
        result += format_value_stylish(key, unchanged, depth)
        result += "\n"
    if "children" in value_diff:
        result += "    " * depth + f"    {key}: "
        result += generate_diff_stylish(children, depth + 1)
        result += "\n"
    return result


def generate_diff_stylish(diff_dict, depth=0):
    result = "{\n"
    for key, value in diff_dict.items():
        result += generate_value_diff_stylish(key, value, depth)
    result += "    " * depth + "}"
    return result
