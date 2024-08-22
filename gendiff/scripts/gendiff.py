import argparse
import json

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


def open_json_file(path):
    with open(path, 'r') as f:
        file_content = f.read()
    data = json.loads(file_content)
    return data


def load_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f, object_hook=json_obj_to_python)
        return data


def convert_value(value):
    if value is False:
        return "false"
    elif value is True:
        return "true"
    elif value is None:
        return "null"
    else:
        return value


def json_obj_to_python(obj):
    if isinstance(obj, dict):
        return {k: json_obj_to_python(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [json_obj_to_python(x) for x in obj]
    else:
        return convert_value(obj)


def gendiff(path1, path2):
    data3 = []
    data1 = load_json(path1)
    print(data1)
    data2 = load_json(path2)
    print(data2)
    all_keys = sorted(set(data1.keys() | data2.keys()))
    for key in all_keys:
        value_1 = data1.get(key)
        value_2 = data2.get(key)
        if value_1 == value_2:
            data3.append(f"    {key}: {value_1}")
#            data3[key] = value_1
        elif value_1 is None:
            data3.append(f"  + {key}: {value_2}")
#            data3['+ ' + key] = value_2
        elif value_2 is None:
            data3.append(f"  - {key}: {value_1}")
#            data3['- ' + key] = value_1
        else:
            data3.append(f"  - {key}: {value_1}")
            data3.append(f"  + {key}: {value_2}")
#            data3['- ' + key] = value_1
#            data3['+ ' + key] = value_2
#    print(json.dumps(data3, indent=2))
    print("{\n" + "\n".join(data3) + "\n}")
    return "{\n" + "\n".join(data3) + "\n}"


def sum(a, b):
    return a + b


def main():
    parser()
#   poetry run gendiff file1.json file2.json
#    start()


if __name__ == "__main__":
    main()
