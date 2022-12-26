#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 元组.py
# @time: 2021/11/20 9:57
# @desc:
print("------------------------元组--------------------------")
'''
区别：
    列表  [10,20,30]
    元组  (10,20,30)
'''
print("------------------------元组 创建方式--------------------------")
'''
    1、使用()
    2、tuple()
        如果元组中只有一个元素，逗号不能省
'''

t1 = ('11', '22', '33')
t2 = '11', '22', '33'
t3 = '11',
t4 = ('11')  # 字符串
t5 = ('11',)
# t0 = tuple('11','22','33') # TypeError: tuple expected at most 1 argument, got 3
t01 = tuple(('11', '22', '33'))
print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))
print(t4, type(t4))
print(t5, type(t5))
# print(t0)
print(t01, type(t01))

# 空列表
list1 = []
list2 = list()
# 空字典
d = {}
d = dict()
# 空元组
t = ()
t = tuple()

print("--------元组是不可变序列，不能修改元素，但可以修改元素的元素---------")
print("--------元组遍历---------")
'''
    两种方式
        第一：通过索引 a[1]
        第二：通过遍历 
'''

