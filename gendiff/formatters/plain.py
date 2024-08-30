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
            case 'removed':
                string = f'Property \'{new_path_string}\' was removed'
                result.append(string)
            case 'added':
                value = to_str(item['value'])
                string = f'Property \'{new_path_string}\' was added '\
                    f'with value: {value}'
                result.append(string)
            case 'updated':
                old_value = to_str(item['old_value'])
                new_value = to_str(item['new_value'])
                string = f'Property \'{new_path_string}\' was updated. '\
                    f'From {old_value} to {new_value}'
                result.append(string)
            case _:
                pass
    return result


def to_str(value):
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
