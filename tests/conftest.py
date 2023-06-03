import os
import pytest

@pytest.fixture
def files():
    current_dir = os.path.dirname(__file__)
    result_path_stylish = os.path.join(current_dir, 'fixtures/result_stylish.txt')
    result_path_plain = os.path.join(current_dir, 'fixtures/result_plain.txt')
    result_path_json = os.path.join(current_dir, 'fixtures/result_json.json')
    file1_path_json = os.path.join(current_dir, 'fixtures/file1.json')
    file2_path_json = os.path.join(current_dir, 'fixtures/file2.json')
    file1_path_yaml = os.path.join(current_dir, 'fixtures/file1.yml')
    file2_path_yaml = os.path.join(current_dir, 'fixtures/file2.yaml')
    return (result_path_stylish, result_path_plain,
            result_path_json, file1_path_json, 
            file2_path_json, file1_path_yaml,
            file2_path_yaml)