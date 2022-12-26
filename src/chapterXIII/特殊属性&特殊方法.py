#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 特殊属性&特殊方法.py
# @time: 2021/11/27 16:21
# @desc:
'''
    特殊属性：由双下划线开头双下划线结束
        通过dir(object)查看属性
'''

print(dir(object))

'''
    特殊方法：
        __add__：重写该方法
        __new__与__init__的区别:
            __new__在前创建对象，__init__在后，为实例属性赋值
        
'''
