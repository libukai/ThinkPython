# @Author: Libukai
# @Date:   2018-02-24 23:29:43
# @Last modified by:   likai
# @Last modified time: 2018-02-25 22:40:08


# !/usr/bin/env python
# -*- coding: utf-8 -*-

def print_spam(arg):
    print(arg)
    print(arg)


def do_twice(func, arg):
    func(arg)
    func(arg)


def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)


do_twice(print_spam, 'spam')
print('')
do_four(print_spam, 'spam')


# def do_twice(func, arg):
#     """Runs a function twice.
#
#     func: function object
#     arg: argument passed to the function
#     """
#     func(arg)
#     func(arg)
#
#
# def print_twice(arg):
#     """Prints the argument twice.
#
#     arg: anything printable
#     """
#     print(arg)
#     print(arg)
#
#
# def do_four(func, arg):
#     """Runs a function four times.
#
#     func: function object
#     arg: argument passed to the function
#     """
#     do_twice(func, arg)
#     do_twice(func, arg)
#
#
# do_twice(print_twice, 'spam')
# print('')
#
# do_four(print_twice, 'spam')
