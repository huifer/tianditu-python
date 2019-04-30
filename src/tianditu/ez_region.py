#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __file__: ez_region

import requests
import json
import pymongo

def download_region():
    """
    简易的天地图行政区下载
    :return: null
    """

    client = pymongo.MongoClient(host='localhost', port=27017)

    db = client.lvyou
    collection = db.tianditu_zhongguo_region

    r = requests.get(
        'http://api.tianditu.gov.cn/administrative?postStr={"searchWord":"中国","searchType":"1","needSubInfo":"true","needAll":"true","needPolygon":"true","needPre":"true"}&tk=a4ee5c551598a1889adfabff55a5fc27')

    data = json.loads(r.text)
    data = data['data']
    for item in data:
        child_list = item['child']
        for chi in child_list:
            collection.insert(chi)

if __name__ == '__main__':
    download_region()