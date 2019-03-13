# This code use the standar libairy to pase the html 
from urllib.request import urlopen
import re

# decode chinese
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])

res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
print("\nPage paragraph is: ", res[0])
# 可以看到这里出来的结果还是带有超链接


res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)

