from gendiff import generate_diff
import os
import pytest
from json import JSONDecodeError


def test_generate_diff(filenames):
    (result_path_stylish, result_path_plain,
     result_path_json, file1_path_json,
     file2_path_json, file1_path_yaml,
     file2_path_yaml) = filenames
    result_stylish = open(result_path_stylish).read()
    assert result_stylish == generate_diff(file1_path_json, file2_path_yaml)
    result_plain = open(result_path_plain).read()
    assert result_plain == generate_diff(file1_path_yaml,
                                         file2_path_json, "plain")
    result_json = open(result_path_json).read()
    assert result_json == generate_diff(file1_path_json,
                                        file2_path_json, "json")
    with pytest.raises(FileNotFoundError):
        generate_diff("wrong_path.json", "wrong_path.yaml")
    with pytest.raises(ValueError) as error:
        generate_diff(result_path_stylish, file1_path_json)
        assert "wrong_file_format" in str(error.value)
        generate_diff(file1_path_yaml, file2_path_yaml, "wrong")
        assert "wrong_display_format" in str(error.value)
    current_dir = os.path.dirname(__file__)
    incorrect_json_path = os.path.join(current_dir,
                                       "fixtures/incorrect_json.json")
    with pytest.raises(JSONDecodeError):
        generate_diff(file1_path_json, incorrect_json_path)
