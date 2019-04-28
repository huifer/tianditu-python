#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __file__: edge
# 图像边缘检测
import numpy as np
import cv2


def edge(pic_path):
    image = cv2.imread(pic_path)
    kernel = np.array([
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1],
    ])

    edges = cv2.filter2D(image, -1, kernel)
    cv2.imwrite("./res/edges.jpg", edges)


if __name__ == '__main__':
    path = './res/river_color_bg.png'
    edge(pic_path=path)
