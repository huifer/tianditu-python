#! /usr/bin/env python
# -*- coding: utf-8 -*-

xsq = "120.22940239501227;30.226915680225147;120.28948387694587;30.146807031535218"

xsqlist = xsq.split(";")

xsq_x_list = []
xsq_y_list = []

for i in range(len(xsqlist)):
    if i % 2 == 0:
        xsq_x_list.append(float(xsqlist[i]))
    else:
        xsq_y_list.append(float(xsqlist[i]))

xsq_x_y_list = []

for x, y in zip(xsq_x_list, xsq_y_list):
    xsq_x_y_list.append([float(x), float(y)])

MINX = min(xsq_x_list)
MAXX = max(xsq_x_list)
MINY = min(xsq_y_list)
MAXY = max(xsq_y_list)

print([MINX, MINY])
print([MINX, MAXY])
print([MAXX, MAXY])
print([MAXX, MINY])
print([MINX, MINY])

