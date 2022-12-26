#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 列表.py
# @time: 2021/11/18 22:31
# @desc:
'''
    列表 的两种创建方式
'''
# 方式1
list1 = ['hello', "world", 123, 2.1]
# 方式2
list2 = list(['hello', 'world'])

print('方式1：', list1)
print('方式2：', list2)

print(type(list1[-2]))
# 获取元素索引
print(list1.index(123))
# print(list1.index('hello1', 0, 2)) 元素不在列表存在，报错： ValueError: 'hello1' is not in list


print('------------------------列表切片，语法 list[start:stop:step]---------------------------')
list3 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
listPart = list3[1:5:1]
print(listPart)

print('------------------------列表 判断对象是否存在 in  not in---------------------------')

print(100 in list3)
print(100 not in list3)

print('------------------------列表 添加---------------------------')
'''
    append 列表后追加
    extend 列表末尾至少添加一个元素
    insert 列表任意位置添加一个元素
    切片    列表任意位置添加至少一个元素
'''
# 一、append
appendList = [10, 20, 30]
print('添加之前：', appendList, id(appendList))
appendList.append(50)
print('添加之前：', appendList, id(appendList))

# 二、extend 如果添加的对象时数组，使用append会把数组当做一个对象添加进去，如果使用extend，会把数组中的对象扩展添加进去
extendList = ['HELLO', 'world']
# appendList.append(extendList)
appendList.extend(extendList)
print(appendList)

# 三、 insert 在指定索引位置添加元素
appendList.insert(1, 'insert的元素')
print(appendList)

# 四、切片 在任意位置添加N个元素，
list4 = ['a', 'b', 'c', 'd', 'e', 'f']
list5 = [0, 1, 2, 3]
print(list4)
# 在索引1到3之间插入list5
list4[1:3] = list5
print(list4)

print('------------------------列表 删除---------------------------')
'''
    remove() 移除一个元素 eg: remove(50)
    pop() 根据索引移除元素,不指定索引，移除最后一个元素 eg: pop(1)
    list[1:3] 切片删除，产生新列表(切片的元素，切哪些，哪些就放到新列表)  ;
        如果不产生新列表，用[]替代切片位置 eg: list[1:3] = []
    clear() 清楚列表 eg：list.clear()
    del() 删除列表
'''
listQie1 = [10, 20, 30, 40, 50]
listNewQie = listQie1[1:3]
print("原始元素：", listQie1)
print("切片之后产生的元素：", listNewQie)
listQie1[1:3] = []
print(listQie1)

print('------------------------列表 修改---------------------------')
'''
    根据索引修改对应位置的元素
'''
listUpdate = [10, 20, 30, 40]
listUpdate[2] = 100
print(listUpdate)
listUpdate[2:3] = [111, 222, 333, 444]
print(listUpdate)

print('------------------------列表 排序---------------------------')
"""
    排序：list.sort() 升序 list.sort(reverse=True) 降序
        sorted
"""

listQuery = [10, 30, 20, 4]
listSort = sorted(listQuery)
print(listQuery)
print(listSort)

print('------------------------列表生成式---------------------------')
'''
    语法：list = [i*i for i in range(1,10)] for循环range中的对象产生自定义变量i，然后将i添加到列表
'''

listSheng = [i for i in range(1, 11)]
print(listSheng)
