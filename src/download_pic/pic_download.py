#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from PIL import Image
import os

# 文件存放位置设置
BASE_PATH = os.path.join(os.path.abspath(os.curdir), 'disc')
BASE_PATH_res = os.path.join(os.path.abspath(os.curdir), 'result')

# 简单反爬虫 , 可以不写
headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
}


def download_pic(x, y, z):
    """
    下载地图
    :param x: x 范围
    :param y: y 范围
    :param z: int
    """
    try:
        # 下载图片
        key = 'your tianditu key'
        for xi in x:
            for yi in y:
                url = "http://t3.tianditu.gov.cn/DataServer?T=vec_w&x={}&y={}&l={}&tk={}".format(xi, yi, z, key)
                # 保存文件名称
                fileName = os.path.join(BASE_PATH, "x={}y={}z={}.png".format(xi, yi, z))
                # 具体下载操作
                if (os.path.exists(fileName)) == False:
                    r = requests.get(url=url, headers=headers)
                    if r.status_code == 200:
                        with open(fileName, 'wb') as f:
                            for chunk in r:
                                f.write(chunk)
                    else:
                        print("访问异常")
    except Exception as e:
        print(e)
        pass


def merge_pic(x, y, z):
    """
    合并下载地图
    :param x: x 范围
    :param y: y 范围
    :param z: int
    :return:
    """
    picSize = 256
    try:
        # 构造平图矩阵
        li = []

        for xi in x:
            lis = []
            for yi in y:
                fileName = os.path.join(BASE_PATH, "x={}y={}z={}.png".format(xi, yi, z))
                lis.append(fileName)

            li.append(lis)

        oca = len(x)
        ocb = len(y)

        toImage = Image.new('RGBA', (oca * picSize, ocb * picSize))

        for i in range(oca):
            for j in range(ocb):
                fromImge = Image.open(li[i][j])
                picx = 256 * i
                picy = 256 * j
                loc = (picx, picy)
                toImage.paste(fromImge, loc)

        toImage.save(os.path.join(BASE_PATH_res, "rs.png"))
        print("构造完成输出图片")

    except Exception as e:
        print(e)
        pass


if __name__ == '__main__':
    x = range(27326 - 1, 27333 + 2)
    y = range(13492 - 1, 13507   + 2)
    z = 15
    download_pic(x, y, z)
    merge_pic(x, y, z)
