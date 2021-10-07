"""
DZ 6_4. *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется, не нужно
реально создавать такие большие файлы, это просто задел на будущее проекта). Только теперь не нужно создавать словарь
с данными. Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через двоеточие
и пробел после ФИО:
Иванов,Иван,Иванович: скалолазание,охота
Петров,Петр,Петрович: горные лыжи
"""

from itertools import zip_longest


def load_file(name):
    with open(name, encoding='utf-8') as f:
        return f.read().splitlines()


users = load_file('users.csv')
hobby = load_file('hobby.csv')
cont_users = [i for i in users]
cont_hobby = [i for i in hobby]

with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    if len(cont_hobby) > len(cont_users):
        exit(1)
    else:
        for item_users, item_hobby in zip_longest(cont_users, cont_hobby):
            f.write(f'{item_users}: {item_hobby}\n')
