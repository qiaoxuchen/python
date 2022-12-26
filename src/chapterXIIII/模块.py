#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 模块.py
# @time: 2021/11/28 16:24
# @desc:

'''
    导入的两种方式：
        from 模块名 import 方法名
        import 模块名
    如果有包的话：
        import 包名.模块名

    包和模块的区别：
        包下有__init__.py文件
        模块下没有
'''

import math
import Demo as demo  # form Demo import add

# print(math.pi)


'''
    如果引用的模块中有函数引用的add方法，输出了内容，在当前模块中也引用了add输出了内容，
    如果运行当前模块不想输出引用模块的内容，则把引用模块调用的函数放到__main__方法中；
    语法： if __name__ = '_main_':
            pass
'''
print(demo.add(1, 3))
