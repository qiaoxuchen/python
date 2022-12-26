#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 计算水仙花数.py
# @time: 2021/11/18 21:14
# @desc:

'''

输出100到999之间的水仙花数

desc:153 = 1**3 + 5**3 + 3**3

'''

for item in range(100, 1000, 1):
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100
    if item == ge ** 3 + shi ** 3 + bai ** 3:
        print('一千以内的水仙花：', item)

for item in range(1000, 10000, 1):
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100 % 10
    qian = item // 1000
    if item == ge ** 3 + shi ** 3 + bai ** 3 + qian ** 3:
        print('1000到9999的水仙花：', item)
print("1000到9999没有水仙花")
