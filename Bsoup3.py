# This code use BeautyfulSoup combine with regular expression to find object 

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')

soup = BeautifulSoup(html, features='lxml')

img_links = soup.find_all("img", {"src": re.compile('.*?\.jpg')})   #查找所有img标签 并且包含src属性的对象，
for link in img_links:
    print("Images are:", link['src'])

course_links = soup.find_all('a', {'href': re.compile('https://morvan.*')}) #查找a标签并且带有href超链接的属性，并且内容由匹配的文字开始
for link in course_links:
    print("Links are:", link['href'])
