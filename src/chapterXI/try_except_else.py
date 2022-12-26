#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: try_except_else.py
# @time: 2021/11/24 23:30
# @desc:
'''
    try:
        正常逻辑
    except  错误类型1:
        报错之后的处理逻辑
    except baseException:
        报错之后的处理逻辑
    else:
        如果没有出错，执行该代码体
    finally:
        无论是否报错，都执行该代码体

备注：except 与 else 只执行一个方法体
'''


'''
traceback打印异常：

'''
import traceback

# num2 = 10/0

try:
    print('------')
    num = 10/0
except:
    traceback.print_exc()  # 打印报错日志


