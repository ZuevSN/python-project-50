import argparse
import json

# …




# вывод справки
# по умолчанию есть ключ -h (--help)
# для добавления новых прописываем
# что-то вроде parser.add_argument('count')- это позиционный аргумент
def start():
    parser = argparse.ArgumentParser(description='Compares two configuration \
                                     files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    read(args.first_file,args.second_file)
def read(path1, path2):
    data3 = {}
    data1 = json.load(open(path1))
    print(data1)
    data2 = json.load(open(path2))
    print(data2)
    for key, value in data1.items():
        if key in data2 and data2[key] == value:
            data3[key] = value
        else:
            data3['- ' + key] = value
    for key, value in data2.items():
        if key in data1 and data1[key] == value:
            data3[key] = value
        else:
            data3['+ ' + key] = value
    print('------')
    print(data3)

def main():
    start()
#poetry run gendiff file1.json file2.json
#    start()


if __name__ == "__main__":
    main()
