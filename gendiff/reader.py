import json
import yaml


def process(extension, content):
    match extension:
        case 'json':
            data = json.loads(content)
        case 'yml' | 'yaml':
            data = yaml.safe_load(content)
        case _:
            data = {}
    return data


def read_file(path):
    extension = path.rsplit('.')[-1]
    with open(path, 'r') as f:
        content = f.read()
    data = process(extension, content)
    return data
