import json


def json_format(data):
    result_out = json.dumps(data, indent=4)
    return result_out
