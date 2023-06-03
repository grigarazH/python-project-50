from gendiff.formats.stylish import dict_to_str, format_value_stylish, generate_diff_stylish
from gendiff.gendiff import get_diff_dict
from gendiff.parser import parse_file


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


def test_generate_diff_stylish(files):
    result_path , _, _, file1_path, _, _, file2_path = files
    result = open(result_path).read()
    diff_dict = get_diff_dict(parse_file(file1_path), parse_file(file2_path))
    assert result == generate_diff_stylish(diff_dict)