#!/usr/bin/env python3


from gendiff.cli import parse_cli, print_diff


def main():
    args = parse_cli()
    print_diff(args.first_file, args.second_file, args.format)


if __name__ == "__main__":
    main()
