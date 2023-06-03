from gendiff.formats.stylish import dict_to_str, format_value_stylish, generate_diff_stylish
from gendiff.gendiff import get_diff_dict
from gendiff.parser import parse_file


def test_generate_diff_stylish(files):
    result_path , _, _, file1_path, _, _, file2_path = files
    result = open(result_path).read()
    diff_dict = get_diff_dict(parse_file(file1_path), parse_file(file2_path))
    assert result == generate_diff_stylish(diff_dict)