from gendiff.formats.stylish import generate_diff_stylish
from gendiff.gendiff import get_diff_dict
from gendiff.parser import parse_file


def test_generate_diff_stylish(filenames):
    result_path, _, _, file1_path, _, _, file2_path = filenames
    result = open(result_path).read()
    diff_dict = get_diff_dict(parse_file(open(file1_path)),
                              parse_file(open(file2_path)))
    assert result == generate_diff_stylish(diff_dict)
