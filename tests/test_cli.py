import os
from gendiff.cli import parse_cli


def test_cli(capsys):
    current_dir = os.path.dirname(__file__)
    help_result_path = os.path.join(current_dir, "fixtures/help.txt")
    help_result = open(help_result_path).read()
    try:
        parse_cli(['-h'])
    except SystemExit:
        pass
    output = capsys.readouterr().out
    assert output == help_result
    args_without_format = vars(parse_cli(['file1.json', 'file2.json']))
    assert "stylish" == args_without_format["format"]
    assert "file1.json" == args_without_format["first_file"]
    assert "file2.json" == args_without_format["second_file"]
    args_with_format = vars(parse_cli(['-f', 'plain', 'file1.json', 'file2.json']))
    assert "plain" == args_with_format["format"]
    wrong_arguments_path = os.path.join(current_dir, "fixtures/wrong_arguments.txt")
    wrong_arguments = open(wrong_arguments_path).read()
    try:
        parse_cli(["file.json"])
    except SystemExit:
        pass
    err_output = capsys.readouterr().err
    assert wrong_arguments == err_output
    