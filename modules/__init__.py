# -*- coding: utf-8 -*-

from fibo import fib
import fibo
import sys


# 标准的模块
def standardModules():
    print(sys.version)
    pass


# 内置dir() 方法，找出模块定义
def test_dir():
    s = dir(fibo)
    print(s)
    pass


# 包测试
def test_packages():
    pass


if __name__ == "__main__":
    print(__name__)
    standardModules()
    print('##' * 40)
    test_dir()
    print('##' * 40)
    test_packages()
