from gendiff.formats.plain import format_value_plain, generate_diff_plain
from gendiff.parser import parse_file
from gendiff.gendiff import get_diff_dict


def test_format_value_plain():
    assert format_value_plain({"a": "b", "c": 3}) == "[complex value]"
    assert format_value_plain(True) == "true"
    assert format_value_plain(None) == "null"
    assert format_value_plain(35) == 35
    assert format_value_plain("str") == "'str'"


def test_generate_diff_plain(files):
    _, result_path, _, file1_path, _, _, file2_path = files
    result = open(result_path).read()
    diff_dict = get_diff_dict(parse_file(file1_path), parse_file(file2_path))
    assert result == generate_diff_plain(diff_dict)
