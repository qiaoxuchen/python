#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 作用域.py
# @time: 2021/11/23 23:20
# @desc:

# global修饰的局部变量，变成全局变量；
def fun():
    global age
    name = 'a'
    age = 20
    print(name, type(name))
    print(age, type(age))


fun()
print(age)
