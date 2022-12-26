#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 三行四列的矩形.py
# @time: 2021/11/18 21:51
# @desc:

'''
    输出一个三行四列的矩形
'''

for x in range(3):
    for y in range(4):
        if not bool(x) and y in (0, 3):
            print(end="\t")
        else:
            print('*', end="\t")
    print()
