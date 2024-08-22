import argparse
from gendiff.parse import read_file

# вывод справки
# по умолчанию есть ключ -h (--help)
# для добавления новых прописываем
# что-то вроде parser.add_argument('count')- это позиционный аргумент


def parser():
    parser = argparse.ArgumentParser(description='Compares two configuration \
                                     files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    gendiff(args.first_file, args.second_file)


def fix_value(value):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    else:
        return str(value)


def gendiff(path1, path2):
    data3 = []
    print(path1)
    data1 = read_file(path1)
    print(data1)
    data2 = read_file(path2)
    print(data2)
    all_keys = sorted(set(data1.keys() | data2.keys()))
    for key in all_keys:
        value_1 = data1.get(key)
        value_2 = data2.get(key)
        if value_1 == value_2:
            data3.append(f"    {key}: {fix_value(value_1)}")
        elif value_1 is None:
            data3.append(f"  + {key}: {fix_value(value_2)}")
        elif value_2 is None:
            data3.append(f"  - {key}: {fix_value(value_1)}")
        else:
            data3.append(f"  - {key}: {fix_value(value_1)}")
            data3.append(f"  + {key}: {fix_value(value_2)}")
    print("{\n" + "\n".join(data3) + "\n}")
    return "{\n" + "\n".join(data3) + "\n}"


def temp(path):
    data = read_file(path)
    print(data)


def main():
    parser()
#    temp('file1.yml')


#   poetry run gendiff file1.json file2.json
if __name__ == "__main__":
    main()
