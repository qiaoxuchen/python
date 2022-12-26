#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 递归.py
# @time: 2021/11/24 20:03
# @desc:
'''
    求6的阶乘
'''


def fun(num):
    if num == 1:
        return 1
    else:
        return num * fun(num - 1)


print(fun(10))

'''
    斐波那契数列
'''


def fun2(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return fun2(x - 1) + fun2(x - 2)


print(fun2(6))
