def stylish_format(data):
    result_out = to_str(data)
    return result_out


def to_str(value, depth=0):
    if isinstance(value, dict):
        return unite_lines(value, depth)
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    else:
        return str(value)


def calculate_indent(depth, shift=0):
    return ' ' * (4 * depth + shift)


def unite_lines(data, depth):
    lines = []
    indent = calculate_indent(depth)
    for key, item in data.items():
        line = build_line(key, item, depth + 1)
        lines.append(line)
    return '{\n' + '\n'.join(lines) + '\n' + indent + '}'


def build_line(key, item, depth):
    indent = calculate_indent(depth, -2)
    if isinstance(item, dict):
        value = item.get('value')
        old_value = item.get('old_value')
        new_value = item.get('new_value')
        status = item.get('status')
        match status:
            case 'removed':
                return f"{indent}- {key}: {to_str(value, depth)}"
            case 'added':
                return f"{indent}+ {key}: {to_str(value, depth)}"
            case 'updated':
                return f"{indent}- {key}: {to_str(old_value, depth)}"\
                    f'\n'\
                    f"{indent}+ {key}: {to_str(new_value, depth)}"
            case 'unchanged' | 'nested':
                return f"{indent}  {key}: {to_str(value, depth)}"
            case None:
                return f"{indent}  {key}: {to_str(item, depth)}"
    else:
        return f"{indent}  {key}: {to_str(item, depth)}"
