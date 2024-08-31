def stylish_format(data):
    result = diff_out(data)
    result_out = "{\n" + "\n".join(result) + "\n}"
    return result_out


def diff_out(data, depth=1):
    result = []
    indent = calculate_indent(depth, -2)
    for key, item in data.items():
        if isinstance(item, dict):
            match item.get('status'):
                case 'removed':
                    value = item['value']
                    result.append(
                        f"{indent}- {key}: {to_str(value, depth)}"
                    )
                case 'added':
                    value = item['value']
                    result.append(
                        f"{indent}+ {key}: {to_str(value, depth)}"
                    )
                case 'updated':
                    old_value = item['old_value']
                    new_value = item['new_value']
                    result.append(
                        f"{indent}- {key}: {to_str(old_value, depth)}"
                    )
                    result.append(
                        f"{indent}+ {key}: {to_str(new_value, depth)}"
                    )
                case 'unchanged':
                    value = item['value']
                    result.append(
                        f"{indent}  {key}: {to_str(value, depth)}"
                    )
                case 'nested':
                    result.append(f'{indent}  {key}: {{')
                    result.extend(diff_out(item['value'], depth + 1))
                    result.append(f'{indent}  }}')
                case None:
                    result.append(f"{indent}  {key}: {{")
                    result.extend(diff_out(item, depth + 1))
                    result.append(f"{indent}  }}")
        else:
            result.append(f"{indent}  {key}: {to_str(item, depth)}")
    return result


def calculate_indent(depth, shift=0):
    return ' ' * (4 * depth + shift)


def to_str(value, depth=1):
    if isinstance(value, dict):
        indent = calculate_indent(depth)
        data = diff_out(value, depth + 1)
        return '{\n' + '\n'.join(data) + '\n' + indent + '}'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    else:
        return str(value)
