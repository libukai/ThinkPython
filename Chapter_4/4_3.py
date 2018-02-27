# @Author: likai
# @Date:   2018-02-27 22:22:08
# @Last modified by:   likai
# @Last modified time: 2018-02-27 23:13:15


# !/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import turtle


def triangle(t, r, angle):
    '''
    先绘出一个符合条件的三角形，
    再用同样的三角形进行拼接
    '''
    bottom_angle = (180 - angle) / 2
    t.fd(r)
    t.lt(180 - bottom_angle)
    t.fd(2 * r * math.sin(angle / 180 / 2 * math.pi))
    t.lt(180 - bottom_angle)
    t.fd(r)
    t.lt(180)


def pie(t, n, r):
    '''
    N个相同的三角形拼接即成 Pie 的形状
    '''
    angle = 360 / n
    for i in range(n):
        triangle(t, r, angle)


if __name__ == '__main__':
    bob = turtle.Turtle()
    pie(bob, 9, 100)
    turtle.mainloop()
