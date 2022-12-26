#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: 猜奖活动.py
# @time: 2022/1/2 15:10
# @desc:
import random

ex_num = 0


def fun():
    global ex_num
    while True:
        try:
            guess = int(input("请输入您心中的幸运数字:"))
            result = calculation(guess)
            if result.get('code') == 'success':
                print(result.get('message'))
                break
            else:
                print(result.get('message'))
        except:
            ex_num += 1
            print("\033[31m仅支持输入数字，请重新输入\033[0m")


def calculation(guess):
    if guess > num:
        d = {'code': 'big', 'message': '\033[31m对不起，您猜的有点大了\033[0m😅'}
        return d
    elif guess < num:
        d = {'code': 'small', 'message': '\033[31m对不起，您猜的有点小了\033[0m😆'}
        return d
    else:
        d = {'code': 'success', 'message': '恭喜您猜中了😎'}
        return d


if __name__ == '__main__':
    num = random.randint(1000, 1500)
    print(num)
    type(ex_num)
    fun()
    print('出现了', str(ex_num), '次异常')
    print('出现了%s次异常' % (str(ex_num)))
    print('出现了{0}次异常'.format(ex_num))
    print(f'出现了{ex_num}次异常')  # f==format格式化

