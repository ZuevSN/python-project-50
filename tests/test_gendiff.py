import os
import json
import pytest
from gendiff.generate_diff import generate_diff

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
                raise ValueError(f"Неподдерживаемый формат {file_extension}")
        else:
            return content

def test_gendiff_stylish():
    file_json_1 = get_fixture_path('file1.json')
    file_json_2 = get_fixture_path('file2.json')
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

    result_json = generate_diff(file_json_1, file_json_2)
    assert expected_output == result_json, 'ошибка функции gendiff с плоским json' 
    result_yml = generate_diff(file_yml_1, file_yml_2)
    assert expected_output == result_yml, 'ошибка функции gendiff с плоским yml' 


def test_gendiff_stylish():
    file_json_1 = get_fixture_path('file1_1.json')
    file_json_2 = get_fixture_path('file2_1.json')
    file_yml_1 = get_fixture_path('file1_1.yml')
    file_yml_2 = get_fixture_path('file2_1.yml')
    expected_output = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''
    result_json = generate_diff(file_json_1, file_json_2)
    result_yml = generate_diff(file_yml_1, file_yml_2)
    assert expected_output == result_json, 'ошибка функции gendiff с json'
    assert expected_output == result_yml, 'ошибка функции gendiff с yml'


def test_gendiff_plain():
    file_json_1 = get_fixture_path('file1_1.json')
    file_json_2 = get_fixture_path('file2_1.json')
    file_yml_1 = get_fixture_path('file1_1.yml')
    file_yml_2 = get_fixture_path('file2_1.yml')
    plain_format = 'plain'
    expected_output = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''
    result_json = generate_diff(file_json_1, file_json_2, plain_format)
    result_yml = generate_diff(file_yml_1, file_yml_2, plain_format)
    assert expected_output == result_json, 'ошибка функции gendiff с json формат plain'
    assert expected_output == result_yml, 'ошибка функции gendiff с yml формат plain'


def test_gendiff_json():
    file_json_1 = get_fixture_path('file1_1.json')
    file_json_2 = get_fixture_path('file2_1.json')
    file_yml_1 = get_fixture_path('file1_1.yml')
    file_yml_2 = get_fixture_path('file2_1.yml')
    json_format='json'
    expected_output = '''{
    "common": {
        "status": "nested",
        "value": {
            "follow": {
                "status": "added",
                "value": false
            },
            "setting1": {
                "status": "unchanged",
                "value": "Value 1"
            },
            "setting2": {
                "status": "removed",
                "value": 200
            },
            "setting3": {
                "status": "changed",
                "old_value": true,
                "new_value": null
            },
            "setting4": {
                "status": "added",
                "value": "blah blah"
            },
            "setting5": {
                "status": "added",
                "value": {
                    "key5": "value5"
                }
            },
            "setting6": {
                "status": "nested",
                "value": {
                    "doge": {
                        "status": "nested",
                        "value": {
                            "wow": {
                                "status": "changed",
                                "old_value": "",
                                "new_value": "so much"
                            }
                        }
                    },
                    "key": {
                        "status": "unchanged",
                        "value": "value"
                    },
                    "ops": {
                        "status": "added",
                        "value": "vops"
                    }
                }
            }
        }
    },
    "group1": {
        "status": "nested",
        "value": {
            "baz": {
                "status": "changed",
                "old_value": "bas",
                "new_value": "bars"
            },
            "foo": {
                "status": "unchanged",
                "value": "bar"
            },
            "nest": {
                "status": "changed",
                "old_value": {
                    "key": "value"
                },
                "new_value": "str"
            }
        }
    },
    "group2": {
        "status": "removed",
        "value": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    "group3": {
        "status": "added",
        "value": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
}'''
    result_json = generate_diff(file_json_1, file_json_2, json_format)
    result_yml = generate_diff(file_yml_1, file_yml_2, json_format)
    assert expected_output == result_json, 'ошибка функции gendiff с json формат json'
    assert expected_output == result_yml, 'ошибка функции gendiff с yml формат json'


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
