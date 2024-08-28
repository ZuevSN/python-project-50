def stylish_format(data):
    result = diff_out_heavy(data)
    result_out = "{\n" + "\n".join(result) + "\n}"
    return result_out


def diff_out_heavy(data, depth=1):
    result = []
    space = '    ' * depth
    for key, item in data.items():
        match item.get('status'):
            case 'removed':
                add_to_result(result, f'- {key}', item['value'], depth)
            case 'added':
                add_to_result(result, f'+ {key}', item['value'], depth)
            case 'updated':
                add_to_result(result, f'- {key}', item['old_value'], depth)
                add_to_result(result, f'+ {key}', item['new_value'], depth)
            case 'unchanged':
                string = f"{space}{key}: {fix_value(item['value'])}"
                result.append(string)
            case 'nested':
                result.append(f'{space}{key}: {{')
                result.extend(diff_out_heavy(item['value'], depth + 1))
                result.append(f'{space}}}')
    return result


def add_to_result(result, status_key, value, depth):
    space = '    ' * depth
    if isinstance(value, dict):
        result.append(f'{space[:-2]}{status_key}: {{')
        result.extend(diff_out_light(value, depth + 1))
        result.append(f'{space}}}')
    else:
        string = f'{space[:-2]}{status_key}: {fix_value(value)}'
        result.append(string)
    return result


def diff_out_light(data, depth=1):
    result = []
    for key, item in data.items():
        add_to_result(result, f'  {key}', item, depth)
    return result


def fix_value(value):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    else:
        return str(value)
