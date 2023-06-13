from gendiff.formats.plain import format_value_plain, generate_diff_plain
from gendiff.parser import parse_file, get_file_format
from gendiff.gendiff import get_diff_dict


def test_format_value_plain():
    assert format_value_plain({"a": "b", "c": 3}) == "[complex value]"
    assert format_value_plain(True) == "true"
    assert format_value_plain(None) == "null"
    assert format_value_plain(35) == 35
    assert format_value_plain("str") == "'str'"


def test_generate_diff_plain(filenames):
    _, result_path, _, file1_path, _, _, file2_path = filenames
    result = open(result_path).read()
    file1_content = open(file1_path)
    file1_format = get_file_format(file1_content)
    file2_content = open(file2_path)
    file2_format = get_file_format(file2_content)
    diff_dict = get_diff_dict(parse_file(file1_content, file1_format),
                              parse_file(file2_content, file2_format))
    assert result == generate_diff_plain(diff_dict)
