import os
from gendiff.scripts.gendiff import sum
from gendiff.scripts.gendiff import gendiff

sum_test_cases = [
    (0, 5, 5),
    (0, 0, 0),
    (-5, 0, -5),
    (5, 18, 23),
    (-11, -17, -28),
    (3, -7, -45)
]

@pytest.mark.parametrize("num1, num2, expected_output", sum_test_cases)
def test_sum(num1, num2, expected_output):
    result = sum(num1, num2)
    assert result == expected_output , 'Ошибка функции sum'


gendiff_test_cases = [
    {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": false
    },
    {
        "timeout": 20,
        "verbose": true,
        "host": "hexlet.io"
    },
    {
        '- follow': false,
        'host': 'hexlet.io',
        '- proxy': '123.234.53.22',
        '- timeout': 50,
        '+ timeout': 20,
        '+ verbose': true
    }
]

def get_fixture_path(name):
    return os.path.join('tests/fixtures', name)

def test_gendiff_json():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected_output = get_fixture_path('result.json')
    result = gendiff(file1, file2)
    assert expected_output == result, 'ошибка функции gendiff' 