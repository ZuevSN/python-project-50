from gendiff.parse import read_file
from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.plain import plain_format
from gendiff.formatters.json import json_format


def generate_diff(path1, path2, format='stylish'):
    result = []
    data1 = read_file(path1)
    data2 = read_file(path2)
    tree3 = alt_diff(data1, data2)
    match format:
        case 'stylish':
            result = stylish_format(tree3)
        case 'plain':
            result = plain_format(tree3)
        case 'json':
            result = json_format(tree3)
        case _:
            print('Wrong format')
    return result


def alt_diff(tree1, tree2):
    tree3 = {}
    all_keys = sorted(set(tree1.keys() | tree2.keys()))
    for key in all_keys:
        if key not in tree2.keys():
            tree3[key] = {'status': 'removed', 'value': tree1[key]}
        elif key not in tree1.keys():
            tree3[key] = {'status': 'added', 'value': tree2[key]}
        elif isinstance(tree1[key], dict) and isinstance(tree2[key], dict):
            tree3[key] = {
                'status': 'nested',
                'value': alt_diff(tree1[key], tree2[key])
            }
        else:
            if tree1[key] == tree2[key]:
                tree3[key] = {'status': 'unchanged', 'value': tree1[key]}
            else:
                tree3[key] = {
                    'status': 'changed',
                    'old_value': tree1[key],
                    'new_value': tree2[key]
                }
    return tree3
