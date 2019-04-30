#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __file__: administrative_region
# 天地图行政区获取
import datetime
import requests
import json
import codecs
import pymongo

key = "a4ee5c551598a1889adfabff55a5fc27"

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.lvyou
collection = db.tianditu


def points_calc(shi, points):
    """
    将文本坐标转换成浮点坐标
    :param shi: 市级行政区名称
    :param points: "116.403 39.972,116.402 39.97,116.405 39.97,116.405 39.964,"
    :return: [[x1,y1],[x2,y2]]
    """
    x_list = []
    y_list = []
    for i in points:
        s = [x for x in i['region'].split(",")]
        s = [x.split(' ') for x in s]
        for j in s:
            x_list.append(eval(j[0]))
            y_list.append(eval(j[1]))

    res = [[x, y] for x, y in zip(x_list, y_list)]

    polygon = {'type': 'Polygon', 'coordinates': [res]}
    return polygon


def xianggang_calc(chi):
    """
    处理香港的数据
    :param chi:
    :return:
    """

    for i in chi['child']:
        sheng_point = i['points']
        sheng_name = i['name']
        sheng_reg = points_calc(sheng_name, sheng_point)
        i['geom_tey'] = sheng_reg

    pass


def do_zizhiqu(zz):
    """
    处理自治区
    :param zz: 自治区
    :return:
    """
    for ii in zz:
        # 市区
        s = calc_rege(ii)
        ii['geom_tey'] = s
        cs = ii.get('child')
        if cs:
            for c in cs:
                saa = calc_rege(c)
                c['geom_tey'] = saa
    pass


def calc_rege(chi):
    """
    计算区域
    :param chi:
    :return:
    """
    aomen = chi['name']
    aomen_point = chi.get('points')
    if aomen_point:
        aomen_reg = points_calc(aomen, aomen_point)
        return aomen_reg
    else:
        return None


def run():
    """
    运行函数
    :return:
    """
    r = requests.get(
        'http://api.tianditu.gov.cn/administrative?postStr={"searchWord":"中国","searchType":"1","needSubInfo":"true","needAll":"true","needPolygon":"true","needPre":"true"}&tk=a4ee5c551598a1889adfabff55a5fc27')

    data = json.loads(r.text)

    data['spider_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    data = data['data']
    for item in data:

        child_list = item['child']

        for chi in child_list:
            # 处理的是省
            chi_reg = calc_rege(chi)
            chi['geom_tey'] = chi_reg
            if chi['name'] == '澳门':
                aomen_reg = calc_rege(chi)
                chi['geom_tey'] = aomen_reg
            elif chi['name'] == '香港':
                xianggang_calc(chi)
            else:
                chi_chi = chi['child']
                sheng_point = chi['points']
                sheng_name = chi['name']

                if '自治区' in sheng_name:
                    do_zizhiqu(chi_chi)

                else:
                    for ii in chi_chi:
                        # 市区
                        s = calc_rege(ii)
                        ii['geom_tey'] = s

                        cs = ii.get('child')
                        if cs:
                            for c in cs:
                                saa = calc_rege(c)
                                c['geom_tey'] = saa

            collection.insert(chi)

    pass


if __name__ == '__main__':
    run()
