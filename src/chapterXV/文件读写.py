#!/usr/bin/env python
# encoding: utf-8  修改编码格式
# @author: qiaoxc
# @file: 文件读写.py
# @time: 2021/11/28 17:38
# @desc:

'''
    IO:通过open() 创建文件对象
    语法规则：file = open(filename [,model,encoding])
'''
'''
    r:读取
    w:写
    a:写追加
    b:以二进制方式打开 不能单独使用，需要与其他模式配合使用
    +:以读写方式打开，不能单独使用，需要与其他模式配合使用
    
'''
# file = open('test.txt', 'r', encoding='UTF-8')
# 读取多行
# print(file.readlines())
# file.close()

# 读的文件
src_file = open('qiao.jpg', 'rb')
# 写的文件
target_file = open('two.jpg', 'wb')

target_file.write(src_file.read())

src_file.close()
target_file.close()
