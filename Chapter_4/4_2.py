# @Author: likai
# @Date:   2018-02-26 22:49:00
# @Last modified by:   likai
# @Last modified time: 2018-02-27 00:42:02


# !/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import turtle


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle / 2)


def petal(t, r, angle):
    '''
    每个花瓣绘完的时候，先回归到原来的位置，为下一个花瓣的绘图更便捷的确定偏转角度
    '''
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def flower(t, r, angle, n):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360 / n)


if __name__ == '__main__':
    bob = turtle.Turtle()
    bob.delay = 0.01
    flower(bob, 200, 70, 9)
    turtle.mainloop()
