"""
DZ 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
nginx_logs.txt (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить
список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]
"""
import requests

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
resp = requests.get(url).text
data = resp.splitlines()


def create_tuple(i):
    i_list = i.split()
    return i_list[0], i_list[5].replace('"', ''), i_list[6]


gen = (create_tuple(item) for item in data)
print(list(gen))
