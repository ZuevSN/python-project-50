import pytest
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
@pytest.mark.parametrize("data1, data2, expected_output", data_test_cases)
def test_sum(data1, data2, expected_output):
    result = gendiff(data1, data2)
    assert expected_output == result, 'ошибка функции gendiff' 