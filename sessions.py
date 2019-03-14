#  Turtriol https://morvanzhou.github.io/tutorials/data-manipulation/scraping/3-01-requests/
import requests


def get():  # 发送一个Get 请求
    print('\nget')
    param = {"wd": "莫烦Python"}
    r = requests.get('http://www.baidu.com/s', params=param)
    print(r.url)
    print(r.text)


def post_name():  # 发送一个Post请求
    print('\npost name')
    # http://pythonscraping.com/pages/files/form.html
    data = {'firstname': '莫烦', 'lastname': '周'}  # 目标请求接受两个变量，firstname 和lastname
    r = requests.post('http://pythonscraping.com/files/processing.php', data=data)
    print(r.text)


def post_image():
    print('\npost image')
    # http://pythonscraping.com/files/form2.html
    file = {'uploadFile': open('./image.png', 'rb')}
    r = requests.post('http://pythonscraping.com/files/processing2.php', files=file)
    print(r.text)


def post_login():  # 使用cookies 方法保持登录 （同一网站内）
    print('\npost login')
    # http://pythonscraping.com/pages/cookies/login.html
    payload = {'username': 'Morvan', 'password': 'password'}
    r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
    print(r.cookies.get_dict())
    # http://pythonscraping.com/pages/cookies/profile.php
    r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)  # 指明使用刚才登陆后获取的Cookies
    print(r.text)


def session_login():    # 使用session 方法来保持登录（同一网站内）
    print('\nsession login')
    # http://pythonscraping.com/pages/cookies/login.html
    session = requests.Session()        # 实例一个session
    payload = {'username': 'Morvan', 'password': 'password'}
    r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)  # 并用刚才实例的session去进行web post请求
    print(r.cookies.get_dict())
    r = session.get("http://pythonscraping.com/pages/cookies/profile.php")  # 继续使用同一个session去进行下一步web get 请求
    print(r.text)


get()
post_name()
post_image()
post_login()
session_login()