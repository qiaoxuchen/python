#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 字符串的驻留机制.py
# @time: 2021/11/22 21:08
# @desc:

'''
    字符串驻留机制：
        Python的驻留机制对相同的字符串只保留一份拷贝，后续创建相同字符串时，
        不会开辟新空间，而是把该字符串的地址赋给新创建的变量
'''
