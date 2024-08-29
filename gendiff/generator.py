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
                    'status': 'updated',
                    'old_value': data1[key],
                    'new_value': data2[key]
                }
    return data3
