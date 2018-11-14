# _*_  coding: utf-8 _*_
import requests
from lxml import html
from bs4 import BeautifulSoup

login_url = "http://fanfou.com/login"
url = 'http://fanfou.com/login?fr=%2Flogin'
url_home = 'http://fanfou.com/lovelemontea'



headers_get = {
    'Host': 'fanfou.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT': '1',
    'Referer': 'http://fanfou.com/',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'
    }

headers_login = {
    'Host': 'fanfou.com',
    'Connection': 'keep-alive',
    'Content-Length': '163',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://fanfou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT': '1',
    'Referer': 'http://fanfou.com/',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'
    }

session_requests = requests.session()

# resp = session_requests.get(login_url, headers=headers_get)

# url_from = BeautifulSoup(resp.content, "lxml").find('input', attrs={'name':'urlfrom'})['value']
payload ={
    "loginname": "****",
    "loginpass": "****",
    "token": "7b449665",
    "action": "login",
    # 'urlfrom': url_from,
}

res = session_requests.post(url, data=payload, headers=headers_login)

# print(res, '\nres')


def handle_page(s, url, x):
    res_home = s.get(url)
    soup = BeautifulSoup(res_home.content, "lxml")
    contents = soup.select(' ol > li')
    for content in contents:
        text = content.text
        f = open('text.txt', 'a')
        f.write(text + '\n')
        if x == 17:
            f.close()


# handle_page(session_requests, url_home)

for x in range(1, 17):
    handle_page(session_requests, 'http://fanfou.com/lovelemontea/p.' + str(x) ,x)
