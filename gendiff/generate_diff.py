from gendiff.reader import read_file
from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.plain import plain_format
from gendiff.formatters.json import json_format


def generate_diff(path1, path2, format='stylish'):
    result = []
    data1 = read_file(path1)
    data2 = read_file(path2)
    data3 = generate_dict(data1, data2)
    match format:
        case 'stylish':
            result = stylish_format(data3)
        case 'plain':
            result = plain_format(data3)
        case 'json':
            result = json_format(data3)
        case _:
            print('Wrong format')
    return result


def generate_dict(data1, data2):
    data3 = {}
    all_keys = sorted(set(data1.keys() | data2.keys()))
    for key in all_keys:
        if key not in data2.keys():
            data3[key] = {'status': 'removed', 'value': data1[key]}
        elif key not in data1.keys():
            data3[key] = {'status': 'added', 'value': data2[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            data3[key] = {
                'status': 'nested',
                'value': generate_dict(data1[key], data2[key])
            }
        else:
            if data1[key] == data2[key]:
                data3[key] = {'status': 'unchanged', 'value': data1[key]}
            else:
                data3[key] = {
                    'status': 'changed',
                    'old_value': data1[key],
                    'new_value': data2[key]
                }
    return data3
