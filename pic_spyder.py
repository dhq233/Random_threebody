# -*- coding: utf-8 -*-
"""
Spyder Editor Du

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup  # 应该大写 BeautifulSoup
import os

ua1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
headers = {"user-agent": ua1}

url = "https://cn.bing.com/images/search?q=%E4%B8%89%E4%BD%93%20%E5%A3%81%E7%BA%B8&form=IQFRML&first=1"
#url = "https://0x9.me/CNozT"
res = requests.get(url, headers=headers)

conten = BeautifulSoup(res.text, 'html.parser')
data = conten.find_all("div", attrs={'class': 'img_cont hoff'})  #针对bing
#data = conten.find_all("div", attrs={'class': 'main_img img-hover'})  #针对百度
picture_list = []
n = 0

for d in data:
    n += 1
    plist = d.find("img")
    #print(n, plist)

    if plist != None:
        # if n >= 13:
        #     picture_list.append(plist['data-src'])
        # else:
            picture_list.append(plist['src'])

for i in range(len(picture_list)):
    print("pic:" + picture_list[i], end='\n')

if not os.path.exists(r'data'):
    os.mkdir(r'data')
n = 0
for i in picture_list:
    n += 1
    if i[:5] != 'https':
        continue
    pic = requests.get(i)
    # p_name=i.split('/')[7]

    with open(os.path.join('data/', str(n + 20) + '.webp'), 'wb') as f:
        f.write(pic.content)
