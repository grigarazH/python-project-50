from gendiff.gendiff import generate_diff, get_diff_dict
from gendiff.parser import parse_json
import os


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
    file1_path = os.path.join(current_dir, 'fixtures/file3.json')
    file2_path = os.path.join(current_dir, 'fixtures/file4.json')
    file1 = parse_json(file1_path)
    file2 = parse_json(file2_path)
    assert result == get_diff_dict(file1, file2)


def test_generate_diff():
    current_dir = os.path.dirname(__file__)
    result_path = os.path.join(current_dir, 'fixtures/result_stylish.txt')
    result = open(result_path).read()
    result2_path = os.path.join(current_dir, 'fixtures/result2_stylish.txt')
    result2 = open(result2_path).read()
    file1_path = os.path.join(current_dir, 'fixtures/file1.json')
    file2_path = os.path.join(current_dir, 'fixtures/file2.yaml')
    file3_path = os.path.join(current_dir, 'fixtures/file3.yml')
    file4_path = os.path.join(current_dir, 'fixtures/file4.json')
    assert result == generate_diff(file1_path, file2_path)
    assert result2 == generate_diff(file3_path, file4_path)
    result_plain_path = os.path.join(current_dir, 'fixtures/result_plain.txt')
    result2_plain_path = os.path.join(current_dir, 'fixtures/result2_plain.txt')
    result_plain = open(result_plain_path).read()
    result2_plain = open(result2_plain_path).read()
    assert result_plain == generate_diff(file1_path, file2_path, "plain")
    assert result2_plain == generate_diff(file3_path, file4_path, "plain")
    result_json_path = os.path.join(current_dir, 'fixtures/result_json.txt')
    result2_json_path = os.path.join(current_dir, 'fixtures/result2_json.txt')
    result_json = open(result_json_path).read()
    result2_json = open(result2_json_path).read()
    assert result_json == generate_diff(file1_path, file2_path, "json")
    assert result2_json == generate_diff(file3_path, file4_path, "json")
    assert "Wrong file format" == generate_diff(result_path, file1_path)
    assert "Wrong display format" == generate_diff(file1_path, file2_path, "wrong")
