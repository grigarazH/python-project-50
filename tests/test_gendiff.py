from gendiff.gendiff import format_bool, get_no_diff_string
from gendiff.gendiff import get_diff_string, get_value_diff, generate_diff
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


def test_generate_diff():
    current_dir = os.path.dirname(__file__)
    result = open(os.path.join(current_dir, 'fixtures/result.txt')).read()
    file1_path = os.path.join(current_dir, 'fixtures/file1.json')
    file2_path = os.path.join(current_dir, 'fixtures/file2.json')
    assert result == generate_diff(file1_path, file2_path)
