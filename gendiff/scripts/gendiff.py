#!/usr/bin/env python3
from gendiff.argument_parser import parse_args
from gendiff.generate_diff import generate_diff


def main():
    first_file, second_file, format = parse_args()
    result = generate_diff(first_file, second_file, format)
    print(result)


if __name__ == "__main__":
    main()
