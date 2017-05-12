#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017\5\12 0012 18:48
# @Author  : Aries
# @desc    : 错误和异常
# @File    : __init__.py
# @Software: PyCharm

class MyError(Exception):
    # ，Exception 默认的 __init__() 被覆盖。新的方式简单的创建 value 属性。
    # 这就替换了原来创建 args 属性的方式。
    def __init__(self, value):
        this.value = value

    def __str__(self):
        return repr(self.value)


# 异常的处理
def testExecption(n):
    try:
        if n > 9:
            # 抛出异常
            raise Exception('spam', 'eggs')
    except Exception as  inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)  # __str__ allows args to be printed directly
    finally:
        print('清理行为')
    pass


def testElseException():
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except IOError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()


# 预定义清理行为
def test():
    with open("myfile.txt") as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    testExecption(10)
    pass
