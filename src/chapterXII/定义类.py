#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 定义类.py
# @time: 2021/11/25 0:37
# @desc:
'''
    模板类
'''


class Student:
    # 类属性
    native_space = '北京'

    # 初始化属性（类似于Java的构造函数） 有默认参数
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    # 实例方法 有默认参数
    def eat(self):
        print('---吃饭---')

    # 静态方法 没有默认参数
    @staticmethod
    def static(a):
        print('---静态方法---', a)

    # 类方法 有默认参数
    @classmethod
    def classMethod(cls):
        print('---类方法---', cls)


# 函数
def hanshu():
    print('---类之外数据函数---')


'''
    Python: 两种方式创建对象，可以直接
        stu = Student('zhangsan', 10, '男')
'''

Student.eat(Student('zhangsan', 10, '男'))
Student.static(0)

stu = Student('zhangsan', 10, '男')
stu.static(110)

# 动态绑定方法
stu.leihanshu = hanshu
stu.leihanshu()

# print(stu.native_space)
# Student.classMethod()
