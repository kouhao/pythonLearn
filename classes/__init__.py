#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2017/5/15 17:59
# @Author  : kh
# @Site    : 
# @desc    : 命名空间与作用域事例；global与nonlocal对变量的绑定
# @File    : __init__.py.py
# @Software: PyCharm

def scope_test():
    def do_local():
        spam = "local spam"  #spam是作用域属于do_local
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"  #spam 作用域不是全局的，也非do_nonlocal的
    def do_global():
        global spam
        spam = "global spam" #spam属于全局，对当前方法没有影响
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)