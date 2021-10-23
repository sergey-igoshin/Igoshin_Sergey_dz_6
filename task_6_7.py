"""
DZ 6_7. *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
передаём ему номер записи и новое значение. При этом файл не должен читаться целиком — обязательное требование.
Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.
"""
import sys


def save_file(obj):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{obj[1]}\n')


def load_file(a):
    with open('bakery.csv', encoding='utf-8') as f:
        line = f.read().splitlines()
        if len(a) == 2:
            return line[int(a[1]) - 1:]
        elif len(a) == 3:
            return line[int(a[1]) - 1:int(a[2])]
        else:
            return line


def save_rename(argm):
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        line = f.readlines()
        if int(argm[1]) > len(line):
            print('Номер записи не существует')
        else:
            f.seek(0)
            f.writelines(line[:int(argm[1]) - 1] + [f'{argm[2]}\n'] + line[int(argm[1]):])


argm = sys.argv[1:]
if argm[0] == 'add_sale':
    save_file(argm)
elif argm[0] == 'show_sales':
    for i in load_file(argm):
        print(i)
elif argm[0] == 'rename_sale':
    save_rename(argm)
else:
    print('Неправильный аргумент')

# python task_6_7.py add_sale 5978,5
# python task_6_7.py show_sales
# python task_6_7.py show_sales 3
# python task_6_7.py show_sales 1 3
# python task_6_7.py rename_sale 1 4567,8
