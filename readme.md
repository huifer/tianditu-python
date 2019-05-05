# 天地图切片地图分类提取
## 开发环境
- python 3.6
- Pillow==5.4.1
- requests==2.21.0

## 开发文档
[中文文档](doc/download_xyzMAP.md)
## 功能
- [下载天地图切片](src/download_pic/pic_download.py)
    - download_pic 下载函数
    - merge_pic 合并函数
- [天地图行政区获取](src/tianditu/ez_region.py)
    - download_region 行政区下载函数, 详细数据字段含义查看[官网](http://lbs.tianditu.gov.cn/server/administrative.html)
- [天地图POI下载](src/tianditu/ez_poi.py)
    - tianditu_poi_download 天地图POI下载函数
- [根据颜色进行分类提取](src/classify/groupIMG.py)
    - img_color_cov 提取函数

- [边缘识别](src/classify/edge.py)
    - edge 边缘识别函数(简易)
    
    
## License
[**Apache**](LICENSE)
