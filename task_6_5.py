"""
DZ 6_5. ***(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя обоих
исходных файлов и имя выходного файла. Проверить работу скрипта.
"""
import sys
from itertools import zip_longest
users_n, hobby_n, out_users_hobby = sys.argv[1:]


def load_file(name):
    with open(name, encoding='utf-8') as f:
        return f.read().splitlines()


users = load_file(users_n)
hobby = load_file(hobby_n)
cont_users = [i for i in users]
cont_hobby = [i for i in hobby]

with open(out_users_hobby, 'w', encoding='utf-8') as f:
    if len(cont_hobby) > len(cont_users):
        exit(1)
    else:
        for item_users, item_hobby in zip_longest(cont_users, cont_hobby):
            f.write(f'{item_users}: {item_hobby}\n')

# python task_6_5.py users.csv hobby.csv out_users_hobby.txt
