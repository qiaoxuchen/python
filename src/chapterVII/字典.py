#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 字典.py
# @time: 2021/11/19 19:17
# @desc:

# 字典
print("----------------字典---------------------------")
'''
可变序列：
    列表 [] 有序可重复
    字典 {} 查找快 hash计算
'''

print("------------------------字典 创建------------------------")
"""
    方式一：scores = {key1:value1，key2:value2}
    方式二：dict(key1=value1,key2=values2)
"""

person = {"name": "zhangsan", "age": 18}
print(person, type(person))

person2 = dict(name="lisi", age='20')
print(person2, type(person2))

print('---空字典----')
dic = {}

print("------------------------字典 获取元素------------------------")
personGet = person["name"]
print(personGet)
print(person.get("sex", "王五"))  # 如果查找的key不存在，则输出默认值：王五

print("------------------------字典 操作元素------------------------")
print('zhangsaner' in person)  # 用来判断可以是否存在
del person["name"]  # 删除指定的键值对
print('删除后的person：', person)
scores = {"zhangsan": 20, "lisi": 40, "wangwu": 80}
scores["chenliu"] = 10  # 如果值存在就修改，不存在则新增
print("scores:", scores)

print("------------------------字典 视图操作------------------------")

'''
python：
    keys 获取所有key   通过list(keys())得到列表
    values 获取所有values
    items 获取所有键值对  通过list(items)得到一个元组列表
java：
    keySet 获取所有键 得到一个数组
    values 获取所有值 得到一个数组
    entrySet 获取所有键值对 
'''
scoresMap = {"zhangsan": 20, "lisi": 40, "wangwu": 80}
scoresKeys = scoresMap.keys()
scoresVlues = scoresMap.values()
print(list(scoresKeys), type(scoresKeys))
print(scoresVlues, type(scoresVlues))
print(scoresMap.items(), type(scoresMap.items()))

print("------------------------字典 遍历------------------------")
scoresMapIter = {"zhangsan": 20, "lisi": 40, "wangwu": 80}
for item in scoresMapIter:
    print(scoresMapIter.get(item))
print("------------------------字典 生成式------------------------")
# zip()
keys = {"Fruit", "books", "others"}
values = {10, 30, 50}

dictgen = {key.upper(): value for key, value in zip(keys, values)}
print(dictgen)