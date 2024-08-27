import json


def json_format(tree):
    result_out = json.dumps(tree, indent=4)
    return result_out
