#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 内置函数.py
# @time: 2021/11/17 21:31
# @desc:

"""
    input()
    range() 所有range()对象占用内存空间都是相同的，只有start，stop，step；
            只有用到时才计算
"""
print('-------------------------range()-------------------------')
#  range()
n = range(9)
print(n)
print(list(n))
n2 = range(1, 10)
print(n2)
n3 = range(1, 10, 2)
print(list(n3))

print(10 in n3)
print(9 not in n3)
print(8 not in n3)


