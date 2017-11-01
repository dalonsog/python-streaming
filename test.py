#!/usr/bin/env python
from pipe import *
from random import randint

TEST_STRING = 'flsdkfjlskdjflksdjfla\r\nsjkfjksajfla'


def capitalize_first(raw_text):
    return raw_text[0].upper() + raw_text[1:]


def split_every_5_chars(raw_text):
    result = ''
    for i in range(len(raw_text)):
        if i % 5 == 0 and i > 0:
            result += ' '
        result += raw_text[i]
    return result


def clean_text(raw_text):
    return raw_text.replace('\r', '').replace('\n', '')


def replace_f_char_with_kittens(raw_text):
    kitten = '(= ^ _ ^ =)'
    return raw_text.replace('f', kitten)


def print_result(raw_text):
    print('---')
    print(raw_text)
    print('---\n')
    return raw_text


if __name__ == '__main__':
    a = Streameable(TEST_STRING).pipe(
        clean_text,
        capitalize_first,
        split_every_5_chars,
        replace_f_char_with_kittens
    ).collect()

    print(" - String processing - ")
    print(a)

    print(" - List processing - ")
    ListStream([8, 3, 2, 5, 4])\
        .map(lambda x: x * 2)\
        .sort()\
        .for_each(print_result)

    lst = [
        {"id": 5, "name": "Dani"},
        {"id": 2, "name": "Dio"},
        {"id": 4, "name": "Ramon"},
        {"id": 1, "name": "Alex"}
    ]

    ListStream(lst).map(
        lambda x: {
            "id": x['id'],
            "name": x['name'],
            "age": randint(18, 30),
            "randomOperation": x['id'] * randint(1, 3) + 6.23
        }
    ).sort(keygetter=lambda x: x['id']).for_each(print_result)
