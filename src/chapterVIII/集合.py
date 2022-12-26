#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 集合.py
# @time: 2021/11/21 14:48
# @desc:

print("----------------------集合 创建-------------------------------")
'''
特别标注：不允许重复,无序
    使用 {1,2}
    使用set()
'''
s = {1, 2, 3, 4, 4, 3, 2}
print(s)
s2 = set(range(1, 10))
print(s2)
print("----------------------集合 pop-------------------------------")
'''
    pop:一次删除一个任意元素，不能指定参数
'''

print("----------------------集合 关系-------------------------------")

print('--判断是否相等--')
s = {1, 2, 3, 4}
s2 = {3, 2, 1, 4}
print(s == s2)
print('--判断是否子集--')
s3 = {1, 3}
s4 = {6, 7}
print(s.issubset(s3))  # s是s3的子集
print(s3.issubset(s))
print(s.issuperset(s2))
print(s.issuperset(s3))
print(s3.issuperset(s))  # 是否超级
print(s.isdisjoint(s2))
print(s.isdisjoint(s3))
print(s.isdisjoint(s4))  # 是否存在交集

print("----------------------集合 生成式-------------------------------")

list = [i for i in range(1, 10)]
keys = {"name", "age"}
values = {"zhangsan", "18"}
dicts = {key: value for key, value in zip(keys, values)}
set = {i for i in range(1, 10)}
print(list, type(list))
print(set, type(set))
print(dicts, type(dicts))
