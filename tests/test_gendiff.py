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

def test_gendiff_json():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
#    expected_output = read_file(get_fixture_path('result.json'), True)
    
    expected_output = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

    result = gendiff(file1, file2)
    assert expected_output == result, 'ошибка функции gendiff' 
#    assert diff_result == result

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