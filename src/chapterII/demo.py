#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: demo.py
# @time: 2021/11/14 11:38
# @desc: 整数类型

from decimal import Decimal

name = 130
age = 13

n1 = 1.1
n2 = 1.2

print(name)
print("id:", id(name))
print("type:", type(name))

print("int运算", n1 + n2)
print(Decimal('1.1') * Decimal('1.2'))
