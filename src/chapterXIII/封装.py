#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 封装.py
# @time: 2021/11/27 13:36
# @desc:
'''
封装：
    Python：没有属性私有关键字，如果不希望被外部使用，则通过 "__+属性名" 设置属性私有 eg：__age
            但是也可以通过 "_+类名+__属性名" 被外部访问 eg: _student__age
            备注：可以通过 dir(stu) 查看类的属性
    Java：四类访问控制符
        public：公共的，所有类都可见；
        protected：受保护的，对同同一包内的类和所有子类可见；
        private：私有的，在同一类中可见；
        default：在同一包内可见；（默认不适用任何修饰符）
        备注：protected与default区别：
            protected主要保护子类的，声明的方法，在子类中，要么声明protected，要么声明public，不能声明private
            default针对于本包设计的，只要在包下的类或接口都可以访问

'''


