#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __file__: 天地图经纬度转换切片索引
import math


def lng_lat_to_title_index(lng, lat, level):
    """
    天地图经纬度转换切片索引
    :param lng: 经度
    :param lat: 纬度
    :param level: 放大级别
    :return: (切片的x索引,切片的y索引)
    """
    x = (lng + 180) / 360
    title_X = math.floor(x * math.pow(2, level))
    lat_rad = lat * math.pi / 180
    y = (1 - math.log(math.tan(lat_rad) + 1 / math.cos(lat_rad)) / math.pi) / 2
    title_Y = math.floor(y * math.pow(2, level))
    return (title_X, title_Y)


def main():
    z = 18
    xy = [120.25871185675187, 30.16739619707534]
    aaa = lng_lat_to_title_index(xy[0], xy[1], z)
    url = 'http://t2.tianditu.gov.cn/DataServer?T=vec_w&x={}&y={}&l={}&tk=a4ee5c551598a1889adfabff55a5fc27'.format(
        aaa[0], aaa[1], z)
    print(url)


if __name__ == '__main__':
   main()
