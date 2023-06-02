from gendiff.formats.plain import format_value_plain, generate_diff_plain
from gendiff.parser import parse_file
from gendiff.gendiff import get_diff_dict
import os


def test_format_value_plain():
    assert format_value_plain({"a": "b", "c": 3}) == "[complex value]"
    assert format_value_plain(True) == "true"
    assert format_value_plain(None) == "null"
    assert format_value_plain(35) == 35
    assert format_value_plain("str") == "'str'"


def test_generate_diff_plain():
    current_dir = os.path.dirname(__file__)
    result_path = os.path.join(current_dir, 'fixtures/result_plain.txt')
    result = open(result_path).read()
    result2_path = os.path.join(current_dir, 'fixtures/result2_plain.txt')
    result2 = open(result2_path).read()
    file1_path = os.path.join(current_dir, 'fixtures/file1.json')
    file2_path = os.path.join(current_dir, 'fixtures/file2.yaml')
    file3_path = os.path.join(current_dir, 'fixtures/file3.yml')
    file4_path = os.path.join(current_dir, 'fixtures/file4.json')
    diff_dict1 = get_diff_dict(parse_file(file1_path), parse_file(file2_path))
    assert result == generate_diff_plain(diff_dict1)
    diff_dict2 = get_diff_dict(parse_file(file3_path), parse_file(file4_path))
    assert result2 == generate_diff_plain(diff_dict2)
