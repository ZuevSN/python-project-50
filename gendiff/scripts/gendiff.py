#!/usr/bin/env python3
import argparse
from gendiff.generate_difference import diff


def generate_diff():
    parser = argparse.ArgumentParser(description='Compares two configuration \
                                     files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default='stylish',
                        help='set format of output')
    args = parser.parse_args()
    result = diff(args.first_file, args.second_file, args.format)
    print(result)


def main():
    generate_diff()


if __name__ == "__main__":
    main()
