#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: Demo1.py
# @time: 2021/11/23 20:40
# @desc:

def cual(oldNum, newNum):
    result = oldNum + newNum
    return result


# *之后，只能使用关键字形参
def fun3(a, b, *, c, d):
    pass


def fun(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


list = [10, 20, 30]
fun(*list)  # *[] *+[] 位置形参
print('----------------')
list2 = {'a': 10, 'f': 20, 'c': 30}  # 形参的key值，必须与实参的参数一一对应，此行报错
fun(**list2)  # *[] *+[] 位置形参
