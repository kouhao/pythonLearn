#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2017/5/15 18:31
# @Author  : kh
# @Site    : 
# @desc    : 类的私有变量的测试
# @File    : testPrivate.py
# @Software: PyCharm


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)