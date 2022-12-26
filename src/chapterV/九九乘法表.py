#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 九九乘法表.py
# @time: 2021/11/18 22:15
# @desc:

for x in range(1,10):
    for y in range(1,10):
        if x >= y:
            print(x, '*', y, '=', x * y, end="\t")
    print()
