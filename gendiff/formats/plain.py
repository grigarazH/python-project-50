def format_value_plain(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value


def generate_value_diff_plain(key, value_diff, path=""):
    removed = value_diff.get("removed")
    added = value_diff.get("added")
    children = value_diff.get("children")
    if "removed" in value_diff and "added" in value_diff:
        return (f"Property '{path}{key}' was updated. "
                f"From {format_value_plain(removed)} "
                f"to {format_value_plain(added)}\n")
    elif "removed" in value_diff:
        return f"Property '{path}{key}' was removed\n"
    elif "added" in value_diff:
        return (f"Property '{path}{key}' was added "
                f"with value: {format_value_plain(added)}\n")
    elif "children" in value_diff:
        return generate_diff_plain(children, path + f"{key}.")
    else:
        return ""


def generate_diff_plain(diff_dict, path=""):
    result = ""
    for key, value in diff_dict.items():
        result += generate_value_diff_plain(key, value, path)
    result = result[0:-1] if path == "" else result
    return result
