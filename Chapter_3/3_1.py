# @Author: Libukai
# @Date:   2018-02-24 22:33:14
# @Last modified by:   likai
# @Last modified time: 2018-02-25 03:55:18


# !/usr/bin/env python
# -*- coding: utf-8 -*-


def right_justify(s):
    print(' ' * (70 - len(s)) + s)


if __name__ == '__main__':
    s = input('input your word: ')
    right_justify(s)
