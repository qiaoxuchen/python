#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 继承.py
# @time: 2021/11/27 14:08
# @desc:
'''
继承：
    Python：多继承
        继承语法：class son(person):  # 不写父类，默认继承object
        如果继承多个父类，尽量避免有相同方法和属性
        方法调用：如果父类和子类有相同的方法或属性，应该使用哪个？
                单继承：子类会覆盖父类，所以会使用子类
                多继承：如果父类有相同的方法，先继承的哪个类，就调用哪个类的方法
        子类调用父类的两种方式：
            方式一：父类.__init__()
            方式二：super().__init__()

    Java：单继承，多实现
        关键字：子类 extends 父类
                A类 implement B接口
        方法调用：如果父类和子类有相同的方法或属性，应该使用哪个？
            这属于子类重写父类的方法，子类会覆盖掉父类，所以以子类为准
        子类调用父类的两种方式：
            方式一：super().方法名
            方式二：如果不是重写的方法，直接调用方法名就可以 eg：parentMethod()
'''


class School(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def parentMethodEat(self):
        print('父类吃', self.name, self.age)

    def A(self):
        print('School被继承的两个父类有相同的方法', self.name, self.age)


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def A(self):
        print('Person被继承的两个父类有相同的方法', self.name, self.age)


# 多继承
class Son(School, Person):
    # 初始化自己
    def __init__(self, name, age, score):
        # 初始化父类
        School.__init__(self, name, age)
        Person.__init__(self, name, age)
        # super(Son, self).__init__(self, name, age)
        # self.name = name
        # self.age = age
        self.score = score

    def sonMethod(self):
        print('子类方法', self.name, self.age, self.score)

    # 方法重写
    # def A(self):
    #     super().A(self) 通过super调用父类的方法
    #     print('父类与子类重复方法', self.name, self.age, self.score)


son = Son("zhagnsan", 18, 100)
# son.sonMethod()
# son.parentMethodEat()
son.A()
