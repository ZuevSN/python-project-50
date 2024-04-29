import argparse


# вывод справки
# по умолчанию есть ключ -h (--help)
#для добавления новых прописываем что-то вроде parser.add_argument('count') - это позиционный аргумент
def main():
    parser = argparse.ArgumentParser(description = 'Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.parse_args()



if __name__ == "__main__":
    main()