#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: Demo.py
# @time: 2021/11/28 16:58
# @desc:

# import math
from math import pow as po


# print(math.pow(2, 3))
# print(math.ceil(9.001))
# print(math.floor(9.999))

# print(po(2,3))

def add(num1, num2):
    return num1.__add__(num2)


if __name__ == '__main__':
    print(add(3, 3))
