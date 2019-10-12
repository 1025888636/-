# encoding: utf-8
"""
@author: Mengrui
@contact: 1025888636@qq.com
@time: 2019/10/10 11:11
@file: 3_DiGui.py
@desc: 递归
"""

def countdown(i):
    print(i)
    if i <=1:
        return
    else:
        countdown(i-1)


countdown(10)