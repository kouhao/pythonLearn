#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math


# @Time    : 2017\5\12 0012 16:13
# @Author  : Aries
# @Site    :
# @desc    : python的输入与输出
# @File    : __init__.py
# @Software: PyCharm

# 输出格式化
def outPutFormat():
    # str() 返回适合人类阅读的形式；repr()返回适合解释器阅读的样式
    s = "Hello World!"
    print(str(s))  # 适合人类阅读
    print(repr(s))  # 适合解释器阅读
    pass


# 通过两个方式格式化输出
# @rjust:返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。
#       如果指定的长度小于字符串的长度则返回原字符串。
def testOutFormat():
    for x in range(1, 11):
        print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
        print(repr(x * x * x).rjust(4))

    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

    # 普通
    print('We are the {} who say "{}!"'.format('knights', 'Ni'))
    # 索引
    print('{0} and {1}'.format('spam', 'eggs'))
    # 关键字
    print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
    # 索引与关键字组合
    print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

    # '!a' (应用 ascii())，'!s' （应用 str() ）和 '!r' （应用 repr() ）可以在格式化之前转换值:
    print('The value of PI is approximately {}.'.format('566'))
    print('The value of PI is approximately {!a}.'.format('566'))
    print('The value of PI is approximately {!s}.'.format('566'))
    print('The value of PI is approximately {!r}.'.format('566'))

    # 字段名后允许可选的 ':' 和格式指令
    print('The value of PI is approximately {0:.3f}.'.format(math.pi))

    # 在字段后的 ':' 后面加一个整数会限定该字段的最小宽度
    print('{0:10} ==> {1:10d}'.format('Sjoerd', 4127))
    print('{0:10} ==> {1:10d}'.format('Sjoerd', 4127000005))
    pass


# 操作符%格式化str
def testOldFormat():
    print('The value of PI is approximately %5.3f.' % math.pi)
    # python格式化字符串
    # %c   格式化字符及其ASCII码
    # %s   格式化字符串
    # %d   格式化整数
    # %u    格式化无符号整型
    # %o   格式化无符号八进制数
    # %x  格式化无符号十六进制数
    # %X  格式化无符号十六进制数（大写）
    # %f  格式化浮点数字，可指定小数点后的精度
    print('The value of PI is approximately %d.' % math.pi)
    # 格式化操作符辅助指令
    # * 定义宽度或者小数点精度
    # - 用做左对齐
    # + 在正数前面显示加号( + )
    # m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
    pass


# 文件读写
def testFileInOutPut():
    # open()方法，返回文件对象，调用需要两个参数fileName,mode
    # mode:'r'表示只读文件；'w' 表示只是写入文件（已经存在的同名文件将被删掉）；'a' 表示打开文件进行追加，
    # 写入到文件中的任何数据将自动添加到末尾;'r+' 表示打开文件进行读取和写入；默认是'r'
    f = open('test.txt', 'w')
    # file.read(szie);读取文件类容；返回字符串；如果到了文件末尾，f.read() 会返回一个空字符串（''）:
    f.read()
    # f.readline() 从文件中读取单独一行，字符串结尾会自动加上一个换行符（ \n ），只有当文件最后一行没有以换行符结尾时，这一操作才会被忽略
    f.readline()
    for line in f:
        print(line, end=' ')

    # f.write(string) 方法将 string 的内容写入文件，并返回写入字符的长度
    f.write('This is a test\n')

    # f.tell() 返回一个整数，代表文件对象在文件中的指针位置，该数值计量了自文件开头到指针处的比特数
    f.write(b'0123456789abcdef')  # 注意：字符串已经转换成为二进制
    i = f.tell();

    # 需要改变文件对象指针话话，使用 f.seek(offset,from_what)。指针在该操作中从指定的引用位置移动 offset 比特，
    # 引用位置由 from_what 参数指定。 from_what 值为 0 表示自文件起始处开始，
    # 1 表示自当前文件指针位置开始，2 表示自文件末尾开始。from_what 可以忽略，其默认值为零，此时从文件头开始:
    f.seek(5)  # Go to the 6th byte in the file
    f.seek(-3, 2)  # Go to the 3rd byte before the end
    pass


if __name__ == "__main__":
    outPutFormat()
    print('##' * 40)
    testOutFormat()
    print('##' * 40)
    testOldFormat()
    print('##' * 40)
    testFileInOutPut()
    pass
