#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __file__: groupIMG
from PIL import Image

river_color = {
    'R': 171,
    'G': 198,
    'B': 239
}

road_color = {
    'R': 254,
    'G': 240,
    'B': 140
}

shan_color = {
    'R': 187,
    'G': 215,
    'B': 141
}


# 要做的内容 过滤到只剩下 上述三种单一颜色

def img_color_cov(img_path, color, new_name):
    """
    颜色提取
    :param img_path: 被提取图片的文件位置
    :param color: 提取的颜色
    :param new_name: 提取后存放的文件位置
    :return:
    """
    i = 1
    j = 1
    img = Image.open(img_path)
    print(img.size)
    print(img.getpixel((4, 4)))

    width = img.size[0]
    height = img.size[1]
    for i in range(0, width):
        for j in range(0, height):
            data = (img.getpixel((i, j)))
            if (data[0] == color.get("R") and data[1] == color.get("G") and data[2] == color.get("B")):
                # img.putpixel((i, j), (255, 0, 0, 255))
                continue
            else:
                img.putpixel((i, j), (255, 255, 255, 255))

    img = img.convert("RGB")
    img.save(new_name)
    print("颜色转换成功")


if __name__ == '__main__':
    img_color_cov("./base_group_pic.png", river_color, "river_color_bg.png")
    img_color_cov("./base_group_pic.png", road_color, "road_color_bg.png")
    img_color_cov("./base_group_pic.png", shan_color, "shan_color_bg.png")
