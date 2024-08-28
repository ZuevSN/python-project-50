import os
import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize("file1, file2, format, expected", [
    ('file1_simple.json', 'file2_simple.json', 'stylish', 'result_simple_stylish'),
    ('file1_simple.yml', 'file2_simple.yml', 'stylish', 'result_simple_stylish'),
    ('file1.json', 'file2.json', 'stylish', 'result_stylish'),
    ('file1.json', 'file2.json', 'plain', 'result_plain'),
    ('file1.json', 'file2.json', 'json', 'result_json'),
    ('file1.yml', 'file2.yml', 'stylish', 'result_stylish'),
    ('file1.yml', 'file2.yml', 'plain', 'result_plain'),
    ('file1.yml', 'file2.yml', 'json', 'result_json'),
])


def test_gendiff(file1, file2, format, expected):
    def get_fixture_path(name):
        return os.path.join('tests/fixtures', name)
    def read_file(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            return content
    expected_result = read_file(get_fixture_path(expected))
    file_1 = get_fixture_path(file1)
    file_2 = get_fixture_path(file2)
    result = generate_diff(file_1, file_2, format)
    assert result == expected_result, f"Неправильный результат функции generate_diff с файлами {file1}, {file2} и форматом {format}."
