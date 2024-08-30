from gendiff.reader import read_file
from gendiff.builder import build_tree
from gendiff.formatters.selector import apply_format


def generate_diff(path1, path2, format='stylish'):
    data1 = read_file(path1)
    data2 = read_file(path2)
    tree = build_tree(data1, data2)
    result = apply_format(format, tree)
    return result
