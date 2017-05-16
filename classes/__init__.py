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
    pass


# 对类的测试
def testClass():
    # MyClass.i 和 MyClass.f 是有效的属性引用，分别返回一个整数和一个方法对象
    # __doc__ 也是一个有效的属性，返回类的文档字符串
    # 注意事项：
    # 数据属性会覆盖同名的方法属性。为了避免意外的名称冲突，这在大型程序中是极难发现的 Bug，
    # 使用一些约定来减少冲突的机会是明智的。可能的约定包括：大写方法名称的首字母，
    # 使用一个唯一的小字符串（也许只是一个下划线）作为数据属性名称的前缀，
    # 或者方法使用动词而数据属性使用名词。
    class MyClass:
        '''A simple example class'''
        i = 12345  # 类变量；可变对象如list作为类变量容易出问题；

        def f(self):
            return 'hello word!'

        # 类初始化时执行
        def __init__(self):
            self.data = 3  # 实例变量

    # 实例化类
    x = MyClass()
    print(x.__doc__)
    print(x.__dict__)
    print(x.__class__)
    print(x.i)
    x.i = 6
    print(x.i)
    print(x.f())
    print(x.data)


# 类的继承
# 函数 isinstance() 用于检查实例类型
# 函数 issubclass() 用于检查类继承
# python 支持多继承形式;
def testExtends():
    # 多继承时，属性是从左至右查询属性
    # super() 可以动态的改变解析顺序
    pass


# 类的私有变量：只能从对像内部访问的“私有”实例变量，在 Python 中不存在；
# 变通方式：以一个下划线开头的命名（例如 _spam ）会被处理为 API 的非公开部分
# （无论它是一个函数、方法或数据成员）
def testprivate():
    class Mapping:
        def __init__(self, iterable):
            self.items_list = []
            self.__update(iterable)

        def update(self, iterable):
            for item in iterable:
                self.items_list.append(item)

        __update = update  # private copy of original update() method

    class MappingSubclass(Mapping):

        def update(self, keys, values):
            # provides new signature for update()
            # but does not break __init__()
            for item in zip(keys, values):
                self.items_list.append(item)

    pass


# 对类各种技术简介
# 类变量:类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
# 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据
# 方法重写：
# 实例变量：定义在方法中的变量，只作用于当前实例的类
# 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待
# 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法

