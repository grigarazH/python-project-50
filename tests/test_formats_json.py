from gendiff.gendiff import get_diff_dict
from gendiff.parser import parse_file, get_file_format
from gendiff.formats.json import generate_diff_json


def test_formats_json(filenames):
    _, _, result_path, file1_path, _, _, file2_path = filenames
    result = open(result_path).read()
    file1_content = open(file1_path)
    file1_format = get_file_format(file1_content)
    file2_content = open(file2_path)
    file2_format = get_file_format(file2_content)
    diff_dict = get_diff_dict(parse_file(file1_content, file1_format),
                              parse_file(file2_content, file2_format))
    assert result == generate_diff_json(diff_dict)
