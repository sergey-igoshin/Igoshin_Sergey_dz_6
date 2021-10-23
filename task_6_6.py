"""
DZ 6_6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом
командной строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки
значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
просто запуск скрипта — выводить все записи;
запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму
числу, включительно.
Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
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


argm = sys.argv[1:]
if argm[0] == 'add_sale':
    save_file(argm)
elif argm[0] == 'show_sales':
    for i in load_file(argm):
        print(i)
else:
    print('Неправильный аргумент')

# python task_6_6.py add_sale 5978,5
# python task_6_6.py show_sales
# python task_6_6.py show_sales 3
# python task_6_6.py show_sales 1 3
