from gendiff.formats.stylish import dict_to_str, format_value_stylish, generate_diff_stylish
from gendiff.gendiff import get_diff_dict
from gendiff.parser import parse_file
import os


def test_dict_to_str():
    dict1 = {
        'a': {
            'b': {
                'c' : 'd'
            }
        }
    }

    assert "{\n    a: {\n        b: {\n            c: d\n        }\n    }\n}" == dict_to_str(dict1)


def test_format_value_stylish():
    dict1 = {
        'a': {
            'b': {
                'c' : 'd'
            }
        }
    }
    assert """key: {
        a: {
            b: {
                c: d
            }
        }
    }""" == format_value_stylish("key", dict1)
    assert "key: true" == format_value_stylish("key", True)
    assert "key: null" == format_value_stylish("key", None)
    assert "key:" == format_value_stylish("key", "")
    assert "key: value" == format_value_stylish("key", "value")


def test_generate_diff_stylish():
    current_dir = os.path.dirname(__file__)
    result_path = os.path.join(current_dir, 'fixtures/result_stylish.txt')
    result = open(result_path).read()
    result2_path = os.path.join(current_dir, 'fixtures/result2_stylish.txt')
    result2 = open(result2_path).read()
    file1_path = os.path.join(current_dir, 'fixtures/file1.json')
    file2_path = os.path.join(current_dir, 'fixtures/file2.yaml')
    file3_path = os.path.join(current_dir, 'fixtures/file3.yml')
    file4_path = os.path.join(current_dir, 'fixtures/file4.json')
    diff_dict1 = get_diff_dict(parse_file(file1_path), parse_file(file2_path))
    assert result == generate_diff_stylish(diff_dict1)
    diff_dict2 = get_diff_dict(parse_file(file3_path), parse_file(file4_path))
    assert result2 == generate_diff_stylish(diff_dict2)