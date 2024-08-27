def plain_format(tree):
    result = diff_out(tree)
    result_out = "\n".join(result)
    return result_out


def diff_out(tree, path_string=None):
    result = []
    for key, item in tree.items():
        temp = path_string
        if item.get('status'):
            path_string = f'{path_string}.{key}' if path_string else key
        match item.get('status'):
            case 'removed':
                result.append(f'Property \'{path_string}\' was removed')
            case 'added':
                result.append(f'Property \'{path_string}\' was added '
                              f'with value: {value_in_string(item['value'])}')
            case 'changed':
                result.append(f'Property \'{path_string}\' was updated. '
                              f'From {value_in_string(item['old_value'])} '
                              f'to {value_in_string(item['new_value'])}')
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
