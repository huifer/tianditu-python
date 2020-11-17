#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __file__: once_download

import requests
import os

# 文件存放位置设置
BASE_PATH = os.path.join(os.path.abspath(os.curdir), 'disc')
print(BASE_PATH)

# 简单反爬虫 , 可以不写
headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
}

# 单个图片的参数
x = 27326
y = 13492
z = 15
key = 'your tianditu key'
# 完整url
url = "http://t3.tianditu.gov.cn/DataServer?T=vec_w&x={}&y={}&l={}&tk={}".format(x, y, z, key)
# 保存文件名称
fileName = os.path.join(BASE_PATH, "x={}y={}z={}.png".format(x, y, z))
# 具体下载操作
if (os.path.exists(fileName)) == False:
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        with open(fileName, 'wb') as f:
            for chunk in r:
                f.write(chunk)
