from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.plain import plain_format
from gendiff.formatters.json import json_format


def apply_format(format, data):
    match format:
        case 'stylish':
            result = stylish_format(data)
        case 'plain':
            result = plain_format(data)
        case 'json':
            result = json_format(data)
        case _:
            print('Wrong format')
    return result
