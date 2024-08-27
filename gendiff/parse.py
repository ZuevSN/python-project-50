import json
import yaml


def load_json(path):
    with open(path, "r") as f:
        data = json.load(f)
        return data


def load_yaml(path):
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
        return data


def read_file(path):
    extension = path.rsplit('.')[-1]
    match extension:
        case 'json':
            data = load_json(path)
        case 'yml' | 'yaml':
            data = load_yaml(path)
        case _:
            data = {}
    return data
