import os
import json
import pytest
#from gendiff.scripts.gendiff import sum
from gendiff.scripts.gendiff import gendiff
#poetry run pytest tests/

def get_fixture_path(name):
    return os.path.join('tests/fixtures', name)

def read_file(file_path, parse=False):
    _, file_extension = os.path.splitext(file_path)
    with open(file_path, 'r') as f:
        content = f.read()
        if parse:
            if file_extension == '.json':
                return json.loads(content)
            else: 
#file_extension == '.yaml':
                raise ValueError(f"Неподдерживаемый формат {file_extension}")
        else:
            return content

def test_gendiff():
    file_json_1 = get_fixture_path('file1.json')
    file_json_2 = get_fixture_path('file2.json')
#    expected_output = read_file(get_fixture_path('result.json'), True)
    file_yml_1 = get_fixture_path('file1.yml')
    file_yml_2 = get_fixture_path('file2.yml')
    expected_output = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

    result_json = gendiff(file_json_1, file_json_2)
    assert expected_output == result_json, 'ошибка функции gendiff с json' 
    result_yml = gendiff(file_yml_1, file_yml_2)
    assert expected_output == result_yml, 'ошибка функции gendiff с yml' 

@pytest.fixture(scope="module")
def module_fixture():
    print("Setup module fixture")
    yield
    print("Teardown module fixture")

def test_one(module_fixture):
    print("Running test_one")

def test_two():
    print("Running test_two")

def test_three(module_fixture):
    print("Running test_three")

#poetry run pytest tests/ -vv