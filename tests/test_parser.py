import pytest
import os
from gendiff.parser import parse_file, parse_json, parse_yaml

@pytest.fixture
def expected():
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
    return dict1, dict2


def test_parse_json(expected):
    current_dir = os.path.dirname(__file__)
    file1_path = os.path.join(current_dir, 'fixtures/file1.json')
    file2_path = os.path.join(current_dir, 'fixtures/file2.json')
    assert expected[0] == parse_json(file1_path)
    assert expected[1] == parse_json(file2_path)


def test_parse_yaml(expected):
    current_dir = os.path.dirname(__file__)
    file1_path = os.path.join(current_dir, 'fixtures/file1.yml')
    file2_path = os.path.join(current_dir, 'fixtures/file2.yaml')
    assert expected[0] == parse_yaml(file1_path)
    assert expected[1] == parse_yaml(file2_path)


def test_parse_file(expected):
    current_dir = os.path.dirname(__file__)
    file1_path_json = os.path.join(current_dir, 'fixtures/file1.json')
    file2_path_json = os.path.join(current_dir, 'fixtures/file2.json')
    assert expected[0] == parse_file(file1_path_json)
    assert expected[1] == parse_file(file2_path_json)
    file1_path_yaml = os.path.join(current_dir, 'fixtures/file1.yml')
    file2_path_yaml = os.path.join(current_dir, 'fixtures/file2.yaml')
    assert expected[0] == parse_file(file1_path_yaml)
    assert expected[1] == parse_file(file2_path_yaml)