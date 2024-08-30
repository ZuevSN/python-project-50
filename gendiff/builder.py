def build_tree(data1, data2):
    result = {}
    all_keys = sorted(set(data1.keys() | data2.keys()))
    for key in all_keys:
        if key not in data2.keys():
            result[key] = {'status': 'removed', 'value': data1[key]}
        elif key not in data1.keys():
            result[key] = {'status': 'added', 'value': data2[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {
                'status': 'nested',
                'value': build_tree(data1[key], data2[key])
            }
        elif data1[key] == data2[key]:
            result[key] = {'status': 'unchanged', 'value': data1[key]}
        else:
            result[key] = {
                'status': 'updated',
                'old_value': data1[key],
                'new_value': data2[key]
            }
    return result
