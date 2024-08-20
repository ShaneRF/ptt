import requests
from bs4 import BeautifulSoup
import time
import pandas
'''
變數準備
'''

# 目標網址
target_url = "https://www.ptt.cc/bbs/"

# 目標看板
target_board = "Tech_Job"

#目標頁面
target_page = "/index"

#目標頁數
page_num = ""

#頁面附屬檔名
page_ext = ".html"

target = target_url + target_board + target_page + page_num  + page_ext

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
}

import requests
data = requests.get(target,headers=headers)
print(data.content)

'''另一種寫法
#def download_html():
    #data = requests.get(target,headers=headers)
    #data = (data.content)
    #return data 
    #return None
'''


def download_html(target,headers):
    return requests.get(target,headers =headers)

def parser_board_urls(requests_):
    #傳入requests_並解析成bs4的物料
    html_code = BeautifulSoup(requests_.content, features="html.parser")
    div_list = html_code.find_all('div', class_='title')
    
    urls = []
    for div_ in div_list:
        try:
            a_tag = div_.find('a').attrs['href']
        except:
            a_tag = None
        urls.append(urls)
    return urls

##Test
a = download_html(target, headers)
b = parser_board_urls(a)
for u in b:
    print(u)
    

def parser_article_content():
    return None

##Test
a=download_html(target,headers)
print(a.content)