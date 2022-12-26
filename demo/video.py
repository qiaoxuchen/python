#!/usr/bin/env python
# encoding: utf-8
# @author: qiaoxc
# @file: video.py
# @time: 2021/11/29 20:40
# @desc:


with open('https://ke.qq.com/webcourse/index.html#cid=3132389&term_id=103255650&taid=10423473313663973&type=1024&vid=5285890810297170203', 'rb') as file:
    with open('withTest.png', 'wb') as target_file:
        target_file.write(file.read())
