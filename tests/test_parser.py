import pytest
from gendiff.parser import parse_file
from json import JSONDecodeError
from yaml import YAMLError
import os


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


def test_parse_file(filenames, expected):
    (_, _, _, file1_path_json, file2_path_json,
     file1_path_yaml, file2_path_yaml) = filenames
    file1_json_content = open(file1_path_json)
    file2_json_content = open(file2_path_json)
    file1_yaml_content = open(file1_path_yaml)
    file2_yaml_content = open(file2_path_yaml)
    assert expected[0] == parse_file(file1_json_content, "json")
    assert expected[1] == parse_file(file2_json_content, "json")
    assert expected[0] == parse_file(file1_yaml_content, "yaml")
    assert expected[1] == parse_file(file2_yaml_content, "yaml")
    current_dir = os.path.dirname(__file__)
    with pytest.raises(FileNotFoundError):
        parse_file(open("wrong_file.json"))
    with pytest.raises(JSONDecodeError):
        incorrect_json_content = open(os.path.join(current_dir,
                                      "fixtures/incorrect_json.json"))
        parse_file(incorrect_json_content, "json")
    with pytest.raises(YAMLError):
        incorrect_yaml_content = open(os.path.join(current_dir,
                                      "fixtures/incorrect_yaml.yaml"))
        parse_file(incorrect_yaml_content, "yaml")
