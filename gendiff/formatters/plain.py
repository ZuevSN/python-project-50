def plain_format(data):
    result = diff_out(data)
    result_out = "\n".join(result)
    return result_out


def diff_out(data, path_string=None):
    result = []
    for key, item in data.items():
        status = item.get('status')
        new_path_string = f'{path_string}.{key}' if path_string else key
        match status:
            case 'nested':
                result.extend(diff_out(item['value'], new_path_string))
            case 'removed' | 'added' | 'updated':
                string = generate_string(new_path_string, status, item)
                result.append(string)
            case _:
                pass
    return result


def generate_string(path_string, status, item):
    string_out = None
    string = f'Property \'{path_string}\' was {status}'
    match status:
        case 'removed':
            string_out = string
        case 'added':
            value = value_in_string(item['value'])
            string_out = f'{string} with value: {value}'
        case 'updated':
            old_value = value_in_string(item['old_value'])
            new_value = value_in_string(item['new_value'])
            string_out = f'{string}. From {old_value} to {new_value}'
    return string_out


def value_in_string(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif isinstance(value, int):
        return str(value)
    else:
        return f'\'{value}\''
