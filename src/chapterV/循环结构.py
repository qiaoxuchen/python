#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 循环结构.py
# @time: 2021/11/18 20:48
# @desc:
'''
    while
    for -in
'''
print('-------------------------while-------------------------')
''' 计算1到100之间的偶数和 '''
sumNum = 0
num = 0
while num < 101:
    if not bool(num % 2):
        sumNum += num
    num += 1
print(sumNum)

a = 2
print(a % 2)
print(bool(a % 2))

print('-------------------------for-in-------------------------')
for item in 'Python':
    print(item)

for i in range(0, 10, 2):
    print(i)

# 如果在循环体中不需要使用到自定义变量，可将自定义变量写“_”
for _ in range(5):
    print("hello world")

for a in range(5):
    print("hello world a")

print("--------------使用for-in计算1到100之间的偶数和-------------")
sumNum2 = 0
for i in range(101):
    if not bool(i % 2):
        sumNum2 += i
print(sumNum2)
