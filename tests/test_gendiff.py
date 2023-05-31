from gendiff.gendiff import format_bool, get_no_diff_string
from gendiff.gendiff import get_diff_string, get_value_diff, generate_diff_for_dicts
from gendiff.gendiff import generate_diff
import os


def test_format_bool():
    assert format_bool(True) == 'true'
    assert format_bool("str") == "str"
    assert format_bool(123) == 123


def test_get_no_diff_string():
    assert get_no_diff_string("key", "value") == "    key: value\n"


def test_get_diff_string():
    assert get_diff_string("key", "value1", None) == "  - key: value1\n"
    assert get_diff_string("key", None, "value2") == "  + key: value2\n"
    correct_value = ("  - key: value1\n" "  + key: value2\n")
    assert get_diff_string("key", "value1", "value2") == correct_value


def test_get_value_diff():
    assert get_value_diff("key", "value", "value") == "    key: value\n"
    assert get_value_diff("key", "value1", None) == "  - key: value1\n"
    assert get_value_diff("key", None, "value2") == "  + key: value2\n"
    correct_value = ("  - key: value1\n" "  + key: value2\n")
    assert get_value_diff("key", "value1", "value2") == correct_value


def test_generate_diff_for_dicts():
    dict1 = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    dict2 = {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }
    current_dir = os.path.dirname(__file__)
    result = open(os.path.join(current_dir, 'fixtures/result.txt')).read()
    assert result == generate_diff_for_dicts(dict1, dict2)


def test_generate_diff():
    current_dir = os.path.dirname(__file__)
    result_path = os.path.join(current_dir, 'fixtures/result.txt')
    result = open(result_path).read()
    file1_path_json = os.path.join(current_dir, 'fixtures/file1.json')
    file2_path_json = os.path.join(current_dir, 'fixtures/file2.json')
    assert result == generate_diff(file1_path_json, file2_path_json)
    file1_path_yaml = os.path.join(current_dir, 'fixtures/file1.yml')
    file2_path_yaml = os.path.join(current_dir, 'fixtures/file2.yaml')
    assert result == generate_diff(file1_path_yaml, file2_path_yaml)
    assert "Wrong format" == generate_diff(result_path, file1_path_json)
