#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: os.py
# @time: 2021/11/28 22:03
# @desc:

'''
    查看官方文档
'''

import os

# 打开文件
# os.system('calc.exe')

# 操作目录
print(os.getcwd())
lst = os.listdir('../chapterXV')
print(lst)
