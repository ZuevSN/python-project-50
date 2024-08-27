import argparse
from gendiff.parse import read_file
from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.plain import plain_format

# вывод справки
# по умолчанию есть ключ -h (--help)
# для добавления новых прописываем
# что-то вроде parser.add_argument('count')- это позиционный аргумент


def parser():
    parser = argparse.ArgumentParser(description='Compares two configuration \
                                     files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default='stylish',
                        help='set format of output')
    args = parser.parse_args()
    gendiff(args.first_file, args.second_file, args.format)


def gendiff(path1, path2, format='stylish'):
    result = []
    print(path1)
    data1 = read_file(path1)
    print(data1)
    data2 = read_file(path2)
    print(data2)
    tree3 = alt_diff(data1, data2)
    print(tree3)
    print(format)
    match format:
        case 'stylish':
            result = stylish_format(tree3)
        case 'plain':
            result = plain_format(tree3)
        case _:
            print('ssss')
    print('===')
#    tree4 = diff_out_easy(tree1)
    print(result)
    return result
    # Пример списка
# Запись списка в файл


def temp_read(path):
    data = read_file(path)
    print(data)
    return data


# создание альтернативного словаря
def alt_diff(tree1, tree2):
    tree3 = {}
    all_keys = sorted(set(tree1.keys() | tree2.keys()))
    for key in all_keys:
        if key not in tree2.keys():
            tree3[key] = {'status': 'removed', 'value': tree1[key]}
        elif key not in tree1.keys():
            tree3[key] = {'status': 'added', 'value': tree2[key]}
        elif isinstance(tree1[key], dict) and isinstance(tree2[key], dict):
            tree3[key] = {
                'status': 'nested',
                'value': alt_diff(tree1[key], tree2[key])
            }
        else:
            if tree1[key] == tree2[key]:
                tree3[key] = {'status': 'unchanged', 'value': tree1[key]}
            else:
                tree3[key] = {
                    'status': 'changed',
                    'old_value': tree1[key],
                    'new_value': tree2[key]
                }
    return tree3

# привести дерево к ожидаемому результату
# каждое погружение в глубину добавляет 4 символа,
# перед этим сделать пробел и написать {
# уменьшение глубины написать }
# def format_stylish(tree, depth):
#    for key, item in tree.items():
# if isinstance(item['value'],dict):
#    result.append(f"{space[:-2]}+ {key}: {{")
#    result.extend(diff_out_easy(item['value'],depth + 1))
#    result.append(f"{space}}}")
# else:
# result.append(f"{space[:-2]}+ {key}: {item['value']}")


def main():
    parser()
#    tree1 = temp_read('file1_1.json')
#    tree2 = temp_read('file2_1.json')
#    tree3 = alt_diff(tree1, tree2)
#    tree4 = diff_out_heavy(tree3)
#    print(tree3)
    print('__________')
#    tree4 = diff_out_easy(tree1)
#    print("{\n" + "\n".join(tree4) + "\n}")
    # Пример списка
# Запись списка в файл
#    with open('output.txt', 'w') as file:
#        for item in tree4:
#            file.write(f"{item}\n")

#    print(tree4)


#   poetry run gendiff file1.json file2.json
if __name__ == "__main__":
    main()
