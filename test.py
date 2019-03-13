# This code is the first test code write by Leo, it use BeautyfulSoup combine with regular expression to find object

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from urllib.request import Request, urlopen

def scrape(link):
    try:
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
        return str(urlopen(Request(link, headers= headers)).read())
    except Exception as e:
        print(str(e))

result = scrape("https://www.funda.nl/koop/verkocht/almere/appartement-40915454-morriganstraat-4/?mna&utm_source=vof_mail&utm_medium=email&utm_campaign=funda&utm_content=object&utm_he=5769078267a7")
print(result)

# if has Chinese, apply decode()
# html = urlopen("https://www.funda.nl/koop/verkocht/almere/appartement-40915454-morriganstraat-4/?mna&utm_source=vof_mail&utm_medium=email&utm_campaign=funda&utm_content=object&utm_he=5769078267a7").read().decode('utf-8')
# # print(html)
# request_page = requests.get("https://www.funda.nl/koop/verkocht/almere/appartement-40915454-morriganstraat-4/?mna&utm_source=vof_mail&utm_medium=email&utm_campaign=funda&utm_content=object&utm_he=5769078267a7")

# soup = BeautifulSoup(request_page, features='lxml')

# # Get all the pictures with
# img_links = soup.find_all("div", {"class": "object-media-foto"})
# for link in img_links:
#     print(link)
# img_links = soup.find_all("img ", {"src": re.compile(r'.*?\.jpg')})   # 查找所有img标签 并且包含src属性的对象，
# img_links = soup.find_all("img ", {"src": re.compile(r'.*?\.jpg')})   # 查找所有img标签 并且包含src属性的对象，
# for link in img_links:
#     print("Images are:", link['src'])

# course_links = soup.find_all('a', {'href': re.compile('https://morvan.*')}) #查找a标签并且带有href超链接的属性，并且内容由匹配的文字开始
# for link in course_links:
#     print("Links are:", link['href'])
