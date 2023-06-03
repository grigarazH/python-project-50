from gendiff import generate_diff
from gendiff.gendiff import get_diff_dict
from gendiff.parser import parse_file, parse_json


def test_generate_diff(files):
    (result_path_stylish, result_path_plain,
     result_path_json, file1_path_json, 
     file2_path_json, file1_path_yaml, 
     file2_path_yaml) = files
    result_stylish = open(result_path_stylish).read()
    assert result_stylish == generate_diff(file1_path_json, file2_path_yaml)
    result_plain = open(result_path_plain).read()
    assert result_plain == generate_diff(file1_path_yaml, file2_path_json, "plain")
    result_json = open(result_path_json).read()
    assert result_json == generate_diff(file1_path_json, file2_path_json, "json")
    assert "Files not found" == generate_diff("wrong_path.json", "wrong_path.yaml")
    assert "Wrong file format" == generate_diff(result_path_stylish, file1_path_json)
    assert "Wrong display format" == generate_diff(file1_path_yaml, file2_path_yaml, "wrong")
