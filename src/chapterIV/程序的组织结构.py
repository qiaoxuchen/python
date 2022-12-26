#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 程序的组织结构.py
# @time: 2021/11/16 21:20
# @desc:

# 顺序结构
# 选择结构
# 循环结构

from decimal import Decimal

"""  对象为False的布尔值  """
print(False)
print(bool(False))
print(bool(''))  # 空字符串
print(bool(""))  # 空字符串
print(bool([]))  # 空数组
print(bool(()))  # 空元组
print(bool(tuple()))  # 空元组
print(bool({}))  # 空字典
print(bool(dict()))  # 空字典
print(bool(set()))  # 空集合

"""  if  """
print("---------------考试成绩-------------------")

score = int(input("请输入一个整数"))

if 90 <= score <= 100:
    otherScore = int(input("请输入综合得分："))
    if 80 <= otherScore <= 100:
        print("你有机会竞选班长")
    elif 60 <= otherScore < 80:
        print("你竞选的可能性很低")
    else:
        print("你没机会")
elif 60 <= score < 90:
    print("B级")
elif 0 <= score < 60:
    print("C级")
else:
    print("成绩有误")

"""   条件表达式   """
print("---------------条件表达式-----------------")
num_a = int(input("输入第一个数："))
num_b = int(input("输入第二个数："))

print("a大" if num_a >= num_b else "b大")

"""  
    pass语句：
        类似于占位符
      """
print("-------------------pass语句-----------------------")
result = "Yes"
if result == "Yes":
    pass
else:
    pass
