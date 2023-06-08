#!/usr/bin/env python3


from gendiff import generate_diff
from gendiff.cli import parse_cli
from json import JSONDecodeError
from yaml import YAMLError


def main():
    args = parse_cli()
    try:
        print(generate_diff(args.first_file, args.second_file, args.format))
    except FileNotFoundError:
        print("Files not found")
    except JSONDecodeError or YAMLError:
        print("Incorrect data in files")
    except ValueError as e:
        if e.args[0] == "wrong_display_format":
            print("Wrong display format")
        else:
            print("Wrong file format")


if __name__ == "__main__":
    main()
