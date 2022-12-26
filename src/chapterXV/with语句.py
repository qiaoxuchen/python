#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: with语句.py
# @time: 2021/11/28 18:18
# @desc:

'''
    with:上下文管理器，即使执行过程失败，也会关闭资源；
    语法： with 上下文表达式 as name:
    上下文表达式实现了__enter__()方法和__exit__()方法
'''

with open('qiao.jpg', 'rb') as file:
    with open('withTest.png', 'wb') as target_file:
        target_file.write(file.read())
