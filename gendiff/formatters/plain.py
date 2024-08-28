def plain_format(data):
    result = diff_out(data)
    result_out = "\n".join(result)
    return result_out


def diff_out(data, path_string=None):
    result = []
    for key, item in data.items():
        temp = path_string
        if item.get('status'):
            path_string = f'{path_string}.{key}' if path_string else key
        match item.get('status'):
            case 'removed':
                string = f'Property \'{path_string}\' was removed'
                result.append(string)
            case 'added':
                value = value_in_string(item['value'])
                string = f'Property \'{path_string}\' was added '\
                    f'with value: {value}'
                result.append(string)
            case 'changed':
                old_value = value_in_string(item['old_value'])
                new_value = value_in_string(item['new_value'])
                string = f'Property \'{path_string}\' was updated. '\
                    f'From {old_value} to {new_value}'
                result.append(string)
            case 'nested':
                if isinstance(item['value'], dict):
                    result.extend(diff_out(item['value'], path_string))
        path_string = temp
    return result


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
