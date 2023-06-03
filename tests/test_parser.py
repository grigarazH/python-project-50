import pytest
import os
from gendiff.parser import parse_file, parse_json, parse_yaml

@pytest.fixture
def expected():
    dict1 = {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": True,
            "setting6": {
                "key": "value",
                "doge": {
                    "wow": ""
                }
            }
        },
        "group1": {
            "baz": "bas",
            "foo": "bar",
            "nest": {
                "key": "value"
            }
        },
        "group2": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    }

    dict2 = {
        "common": {
            "follow": False,
            "setting1": "Value 1",
            "setting3": None,
            "setting4": "blah blah",
            "setting5": {
                "key5": "value5"
            },
            "setting6": {
                "key": "value",
                "ops": "vops",
                "doge": {
                    "wow": "so much"
                }
            }
        },
        "group1": {
            "foo": "bar",
            "baz": "bars",
            "nest": "str"
        },
        "group3": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
    
    return dict1, dict2


def test_parse_file(files, expected):
    _, _, _, file1_path_json, file2_path_json, file1_path_yaml, file2_path_yaml = files
    assert expected[0] == parse_file(file1_path_json)
    assert expected[1] == parse_file(file2_path_json)
    assert expected[0] == parse_file(file1_path_yaml)
    assert expected[1] == parse_file(file2_path_yaml)
    assert parse_file("wrong_path.json") == "file_not_found"
