"""
DZ 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби. Известно, что при
хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи
считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби  (hobby.csv):
скалолазание,охота
горные лыжи
"""
import json


def create_tuple(a, b, i):
    if len(b) > len(a):
        exit(1)
    else:
        if i < len(b):
            return a[i], b[i]
        else:
            return a[i], None


def load_file(name):
    with open(name, encoding='utf-8') as f:
        return f.read().splitlines()


def save_file(obj, name):
    with open(name, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False)


users = load_file('users.csv')
hobby = load_file('hobby.csv')
cont_users = [i for i in users]
cont_hobby = [i for i in hobby]

dictionary = dict(create_tuple(cont_users, cont_hobby, i) for i in range(max(len(cont_users), len(cont_hobby))))
save_file(dictionary, 'dictionary.json')

with open('dictionary.json', encoding='utf-8') as f:
    print(json.load(f))
