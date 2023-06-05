import argparse


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
