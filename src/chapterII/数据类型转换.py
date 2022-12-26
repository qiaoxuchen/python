#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 数据类型转换.py
# @time: 2021/11/14 16:37
# @desc:

name = "乔公子"
age = 18
height = 150.3
wight = '12.342'
s = '10'

print("我叫：" + name + ",今年" + str(age) + "，体重：" + str(height))
print(age)
print(int(height))
print(float(age))
# print(int(wight))   string类型的小数无法转整数，float类型的小数可以转成整数
print(int(s), type(s))
print(float(height))
print(float(wight))
