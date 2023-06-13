import argparse
from gendiff import generate_diff
from json import JSONDecodeError
from yaml import YAMLError


def parse_cli(args=None):
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description=('Compares two '
                                                  'configuration files '
                                                  'and shows a difference.'))
    parser.add_argument('-f', '--format', required=False, metavar='FORMAT',
                        default="stylish",
                        help='set format of output (default: stylish)')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser.parse_args(args)


def get_value_error_string(error):
    if error.args[0] == "wrong_display_format":
        return "Wrong display format"
    else:
        return "Wrong file format"


def print_diff(file_path1, file_path2, format):
    try:
        print(generate_diff(file_path1, file_path2, format))
    except FileNotFoundError:
        print("Files not found")
    except JSONDecodeError or YAMLError:
        print("Incorrect data in files")
    except ValueError as e:
        print(get_value_error_string(e))
