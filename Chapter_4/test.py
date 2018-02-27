# @Author: likai
# @Date:   2018-02-26 21:26:02
# @Last modified by:   likai
# @Last modified time: 2018-02-27 00:36:04


# !/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import turtle


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)


def circle(t, r, n):
    length = 2 * math.pi * r / n
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)


def arc(t, r, n, angle):
    length = 2 * math.pi * r * (angle / 360) / n
    for i in range(n):
        t.fd(length)
        t.lt(angle / n)


r = int(input('请输入圆形的半径：'))
n = int(input('请输入多边形边数：'))
angle = int(input('请输入圆弧的角度：'))
bob = turtle.Turtle()


arc(bob, r, n, angle)
# circle(bob, r, n)
# polygon(bob, length, n)
# square(bob, length)

turtle.mainloop()
