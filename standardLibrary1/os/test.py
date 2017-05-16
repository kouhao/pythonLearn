#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2017/5/15 18:50
# @Author  : kh
# @Site    : 
# @desc    : 操作系统接口
# @File    : test.py
# @Software: PyCharm

import os
print(os.getcwd()) # # Return the current working directory  获取当前操作文件夹路径
os.system('mkdir today')   #执行mkdir的命令

#日常文件与目录管理，用shutil模块
import  shutil

shutil.copyfile('data.db', 'archive.db')  #拷贝文档
shutil.move('/build/executables', 'installdir')  #移动文档

