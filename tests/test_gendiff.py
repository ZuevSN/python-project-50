import os
import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize("file1, file2, format, expected", [
    ('file1_easy.json', 'file2_easy.json', 'stylish', 'result_easy_stylish'),
    ('file1_easy.yml', 'file2_easy.yml', 'stylish', 'result_easy_stylish'),
    ('file1.json', 'file2.json', 'stylish', 'result_stylish'),
    ('file1.json', 'file2.json', 'plain', 'result_plain'),
    ('file1.json', 'file2.json', 'json', 'result_json'),
    ('file1.yml', 'file2.yml', 'stylish', 'result_stylish'),
    ('file1.yml', 'file2.yml', 'plain', 'result_plain'),
    ('file1.yml', 'file2.yml', 'json', 'result_json'),
    ('file1.json', 'file2.yml', 'stylish', 'result_stylish'),
    ('file1.json', 'file2.yml', 'plain', 'result_plain'),
    ('file1.json', 'file2.yml', 'json', 'result_json'),
])
def test_generate_diff(file1, file2, format, expected):
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
    error_string = f'Function generate_diff gave wrong output. '\
        f'Files: {file1}, {file2}. Format: {format}.'
    assert result == expected_result, error_string
