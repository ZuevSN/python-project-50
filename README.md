### Hexlet tests and linter status:
[![Actions Status](https://github.com/ZuevSN/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ZuevSN/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/1286b339dfc75e2e3a88/maintainability)](https://codeclimate.com/github/ZuevSN/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/1286b339dfc75e2e3a88/test_coverage)](https://codeclimate.com/github/ZuevSN/python-project-50/test_coverage)

[![Python CI](https://github.com/ZuevSN/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/ZuevSN/python-project-50/actions/workflows/main.yml)

Проект "Вычислитель отличий" - программа для сравнения двух конфигурационных файлов.

    gendiff [-h] [-f FORMAT] first_file second_file

Результат сравнения может выводится в 3 форматах:
1. **stylish** (формат по умолчанию).
  Вывод строится на основе того, как изменилось содержимое во втором файле относительно первого.
  В случае, если значение по ключу не изменилось будет выведена строка без идентификатора
  В случае измнения значения по ключу - с минусом будет выведено прежнее значение и с плюсом новое значение.
  В случае удаления ключа будет выведена строка с минусом.
  В случание появления нового ключа будет выведена строка с плюсом
  Во всех остальных ситуациях значение по ключу либо отличается, либо ключ есть только в одном файле. 
  Пример

file1.json

        {
          "host": "hexlet.io",
          "timeout": 50,
          "proxy": "123.234.53.22",
          "follow": false
        }
  
  file2.json:
  
        {
          "timeout": 20,
          "verbose": true,
          "host": "hexlet.io"
        }
  
  Результат:
  
        {
          - follow: false
            host: hexlet.io
          - proxy: 123.234.53.22
          - timeout: 50
          + timeout: 20
          + verbose: true
        }

2. **plain**
   В случае этого формата выводится только разница между файлами.
   В случае удаления ключа пишется ,что опция была удалена
   В случае добавления ключа пишется ,что опция была дабавлена с выводом значения
   В случае изменения по ключу выводится старое и новое значение.
   
   Пример вывода:
   
        Property 'common.follow' was added with value: false
        Property 'common.setting2' was removed
        Property 'common.setting3' was updated. From true to null

3. **json**
   В случае этого формата выводится выводится вся информация по 2 файлам с указанием разницы между ними в виде json.

   
Аскинемы с примерами работы:

Шаг 3

Вывод разницы между 2 плоскими json файлами

[![asciicast](https://asciinema.org/a/53c8UhatupgI6HcshMyMgwbNd.svg)](https://asciinema.org/a/53c8UhatupgI6HcshMyMgwbNd)

Шаг 5

Вывод разницы между 2 плоскими yml файлами

[![asciicast](https://asciinema.org/a/XGVmfp2REmOJbiaDiuMOv17rT.svg)](https://asciinema.org/a/XGVmfp2REmOJbiaDiuMOv17rT)

Шаг 6

Вывод результата в формате Stylish для вложенных словарей
[![asciicast](https://asciinema.org/a/pnuGun2d9nEWT7bAz3usmPiZ1.svg)](https://asciinema.org/a/pnuGun2d9nEWT7bAz3usmPiZ1)

Шаг 7

Вывод результата в формате Plain для вложенных словарей

[![asciicast](https://asciinema.org/a/k3hAYVBD1iA18ZXwSB7GidbTM.svg)](https://asciinema.org/a/k3hAYVBD1iA18ZXwSB7GidbTM)

Шаг 8

Вывод результата в виде JSON для вложенных словарей

[![asciicast](https://asciinema.org/a/7E0aiudx1hsi7KSsJrj9mNmia.svg)](https://asciinema.org/a/7E0aiudx1hsi7KSsJrj9mNmia)

    Минимальные требования: Python version 3.8.10; Poetry version 1.8.2
    
    Установка зависимостей проекта: make install
    
    Создание дистрибутива: make build
    
    Установка дистрибутива: make package-install
