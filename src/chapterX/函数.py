#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 函数.py
# @time: 2021/11/23 20:34
# @desc:

'''

def 函数名([输入参数]):
    函数体
    [return xxx]

返回值：
    如果是单个，直接返回类型
    如果是多个，返回结果为元组

'''

'''
参数定义：
Python
    个数可变的位置参数:形参列表中只能定义一个参数 def fun(*args):
        方程式：*args
        返回结果：元组()
    个数可变的关键字形参:形参列表中只能定义一个参数 def fun(**args):
        方程式：**args
        返回结果：字典dict{}
    备注：如果个数可变的位置参数与个数可变的关键字参数同时出现在形参中，
        个数可变的关键字参数必须放在最后一个
Java: public void fun(int ints,String... str){}
    解析：编译时，str会编译成数组，所以不能重载相同数据类型的参数 
        eg: public void fun(int ints,String... str){}; public void fun(int ints,String[] str){}
    方程式：(String... str)
    返回结果：根据定义返回    
'''


def fun3(*args, a, **args2):
    pass


def fun4(a, *args, **args2):
    pass


# 个数可变的关键字形参
def fun2(**args):
    print(args, type(args))


fun2(a=2, b='c', c=['r'], d={'0'})


# 个数可变的位置形参
def fun(*args):
    print(args, type(args))
    print(args[0])


fun(10)
fun(10, 20)
fun(10, 30)


def jisuan(a, b=10):  # b=10 赋默认值
    # print(a,type(a))
    # print(b)
    arg = 100
    p = a.append(arg)
    o = a.append(b)
    print(p)
    print(o)
    print(a)
    print(a)
    return ''


list = [1, 2, 3]
# result2 = jisuan(list,1)
# result = Demo1.cual(10, 20)

# result = Demo1.cual(10, 20)
# print(result)
# print(result2)
