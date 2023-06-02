from gendiff.gendiff import generate_diff, get_diff_dict, generate_diff_stylish
import os
import json


def test_get_diff_dict():
    result = {
        'common': {
            'children': {
                'follow': {
                    'added': False,
                },
                'setting1': {
                    'unchanged': 'Value 1',
                },
                'setting2': {
                    'removed': 200,
                },
                'setting3': {
                    'removed': True,
                    'added': None,
                },
                'setting4': {
                    'added': 'blah blah',
                },
                'setting5': {
                    'added': {
                        'key5': 'value5',
                    },
                },
                'setting6': {
                    'children': {
                        'doge': {
                            'children': {
                                'wow': {
                                    'removed': '',
                                    'added': 'so much',
                                },
                            },
                        },
                        'key': {
                            'unchanged': 'value',
                        },
                        'ops': {
                            'added': 'vops',
                        },
                    },
                },
            },
        },
        'group1': {
            'children': {
                'baz': {
                    'removed': 'bas',
                    'added': 'bars',
                },
                'foo': {
                    'unchanged': 'bar',
                },
                'nest': {
                    'removed': {
                        'key': 'value',
                    },
                    'added': 'str',
                },
            },
        },
        'group2': {
            'removed': {
                'abc': 12345,
                'deep': {
                    'id': 45,
                },
            },
        },
        'group3': {
            'added': {
                'deep': {
                    'id': {
                        'number': 45,
                    },
                },
                'fee': 100500,
            },
        },
    }
    current_dir = os.path.dirname(__file__)
    result_path = os.path.join(current_dir, 'fixtures/result.txt')
    file1_path = os.path.join(current_dir, 'fixtures/file3.json')
    file2_path = os.path.join(current_dir, 'fixtures/file4.json')
    file1 = json.load(open(file1_path))
    file2 = json.load(open(file2_path))
    assert result == get_diff_dict(file1, file2)


def test_generate_diff_stylish():
    current_dir = os.path.dirname(__file__)
    result_path = os.path.join(current_dir, 'fixtures/result2.txt')
    result = open(result_path).read()
    file1_path = os.path.join(current_dir, 'fixtures/file3.json')
    file2_path = os.path.join(current_dir, 'fixtures/file4.json')
    file1 = json.load(open(file1_path))
    file2 = json.load(open(file2_path))
    diff_dict = get_diff_dict(file1, file2)
    assert result == generate_diff_stylish(diff_dict)


def test_generate_diff():
    current_dir = os.path.dirname(__file__)
    result_path = os.path.join(current_dir, 'fixtures/result.txt')
    result = open(result_path).read()
    result2_path = os.path.join(current_dir, 'fixtures/result2.txt')
    result2 = open(result2_path).read()
    file1_path_json = os.path.join(current_dir, 'fixtures/file1.json')
    file2_path_json = os.path.join(current_dir, 'fixtures/file2.json')
    file3_path_json = os.path.join(current_dir, 'fixtures/file3.json')
    file4_path_json = os.path.join(current_dir, 'fixtures/file4.json')
    assert result == generate_diff(file1_path_json, file2_path_json)
    assert result2 == generate_diff(file3_path_json, file4_path_json)
    file1_path_yaml = os.path.join(current_dir, 'fixtures/file1.yml')
    file2_path_yaml = os.path.join(current_dir, 'fixtures/file2.yaml')
    assert result == generate_diff(file1_path_yaml, file2_path_yaml)
    assert "Wrong format" == generate_diff(result_path, file1_path_json)
