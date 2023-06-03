from gendiff.gendiff import get_diff_dict
from gendiff.parser import parse_file
from gendiff.formats.json import generate_diff_json

def test_formats_json(files):
    _, _, result_path, file1_path, _, _, file2_path = files
    result = open(result_path).read()
    diff_dict = get_diff_dict(parse_file(file1_path), parse_file(file2_path))
    assert result == generate_diff_json(diff_dict)