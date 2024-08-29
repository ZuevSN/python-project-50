from gendiff.reader import read_file
from gendiff.generator import generate_dict
from gendiff.formatters.selector import apply_format


def generate_diff(path1, path2, format='stylish'):
    data1 = read_file(path1)
    data2 = read_file(path2)
    data3 = generate_dict(data1, data2)
    result = apply_format(format, data3)
    return result
