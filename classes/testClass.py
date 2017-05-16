#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2017/5/15 18:09
# @Author  : kh
# @Site    : 
# @desc    : 类的演示
# @File    : testClass.py
# @Software: PyCharm

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart



x = Complex(3.0, -4.5)
print(x.r,',',x.i)

#引用与修改
x.counter = 1 #增加事例属性
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
#print(x.counter)

#分割线;类与实例变量
print('##'*40)
class dog:
    kind = 'canine'
    def __init__(self,name):
        self.name= name

d = dog('Fido')
print('d.kind: %s' % d.kind)
print('d.name: %s' % d.name)

#分割线;可变变量做类变量
print('##'*40)
class Dog:
    tricks = []  # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print('d.tricks：{0}'.format(d.tricks))

#分割线;修正变量作为类变量
print('##'*40)
class DogTest:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = DogTest('Fido')
e = DogTest('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print('d.tricks：{0}'.format(d.tricks))