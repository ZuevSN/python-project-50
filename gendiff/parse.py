import json
import yaml


def convert_value(value):
    if value is False:
        return "false"
    elif value is True:
        return "true"
    elif value is None:
        return "null"
    else:
        return value


def json_obj_to_python(obj):
    if isinstance(obj, dict):
        return {k: json_obj_to_python(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [json_obj_to_python(x) for x in obj]
    else:
        return convert_value(obj)


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
