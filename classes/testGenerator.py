#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2017/5/15 18:38
# @Author  : kh
# @Site    : 
# @desc    : 测试生成器
# @File    : testGenerator.py
# @Software: PyCharm


#原理演示
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)

#生成器表达式例子
print(sum(i*i for i in range(10)))
xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)) )


