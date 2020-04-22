#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __file__: ez_tdt_title_download
# 天地图切片下载优化方案
from ez_title_index import lng_lat_to_title_index
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
        key = 'a4ee5c551598a1889adfabff55a5fc27'
        for xi in x:
            for yi in y:
                url = "http://t2.tianditu.gov.cn/DataServer?T=vec_w&x={}&y={}&l={}&tk={}".format(xi, yi, z, key)
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


def run_spider(z, minx, maxx, miny, maxy):
    """
    下载切片地图
    :param z:放大级别
    :param minx: 最小x
    :param maxx: 最大x
    :param miny: 最小y
    :param maxy: 最大y
    :return:
    """
    z = 18
    xy = [minx, miny]
    xxyy = [maxx, maxy]

    minxy = lng_lat_to_title_index(xy[0], xy[1], z)
    maxxy = lng_lat_to_title_index(xxyy[0], xxyy[1], z)
    xr = range(minxy[0] - 1, maxxy[0] + 1)
    yr = range(minxy[1] - 1, maxxy[1] + 1)
    download_pic(xr, yr, z)
    merge_pic(xr, yr, z)


if __name__ == '__main__':
     if os.path.exists(BASE_PATH)==False:
        os.mkdir(BASE_PATH)

    if os.path.exists(BASE_PATH_res) == False:
        os.mkdir(BASE_PATH_res)

    #run_spider(z=6, minx=120.25871185675187, maxx=120.259, miny=30.16739619707534, maxy=30.16741)
    run_spider(z=14, minx=116.55, maxx=116.66, miny=39.94, maxy=39.91)
