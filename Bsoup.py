# This code use third party libaray BeautifualSoup

from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)

soup = BeautifulSoup(html, 'lxml')
print(soup.h1)  # 打印h1标签
print('\n', soup.p)  # 打印P开头的标签

all_href = soup.find_all('a')  # 标签a出现过多次，所以使用find_all来获取全部的a
all_href = [l['href'] for l in all_href]    # for循环去找所有a里面的href超链接
print('\n', all_href)
