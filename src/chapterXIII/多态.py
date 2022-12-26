#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 多态.py
# @time: 2021/11/27 15:59
# @desc:
'''
    Python：动态语言，只要行为相似,可以理解为通过反射的方式调用对象
    Java：静态语言
'''


class Animal(object):
    def eat(self):
        print('动物吃饭')


class Dog(Animal):
    def eat(self):
        print('狗吃屎')


class Cat(Animal):
    def eat(self):
        print("猫吃狗")


class Person():
    def eat(self):
        print('人吃肉')


def fun(obj):
    obj.eat()


fun(Animal())
fun(Dog())
fun(Cat())
fun(Person())
