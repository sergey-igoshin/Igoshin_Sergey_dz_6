"""
DZ 2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
задания.
"""
import requests

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
resp = requests.get(url).text
data = resp.splitlines()


def create_tuple(i):
    i_list = i.split()
    return i_list[0]


ip_list = [create_tuple(item) for item in data]
ip = max(set(ip_list), key=ip_list.count)
print(f'IP адрес спамера {ip}')
print(f'Кол-во отправленных им запросов {ip_list.count(ip)}')
