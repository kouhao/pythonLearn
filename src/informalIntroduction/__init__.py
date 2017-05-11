# -*- coding: utf-8 -*-
#Number

a =1;b =2;
print(a+b)

a = 50-5*6
print(a)

a = (50-5*6)/4  #除法总是返回floating point number
print(a)

a = 17/3
print(a)

a = 17 // 3 #向下取整用符号//
print(a)

a= 17 % 3  #符号 % 取余
print(a)

a  = 5**2 # 符号**计算次方
print(a)

# Strings

a  = 'spam eggs' #单引用
print(a)

a = 'doesn\'t' #用\'来转义单引用
print(a)

a = "doesn't" #多引用,以及使用转义来实现有其他的双引号
print(a)

print('C:\some\name')  #\n 换行
print('C:\some\\name')  #\\转义
print(r'C:\some\name')  #在string前假r,表示引用

print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")  #  字符串保存多行  用"""..."""或者 '''...'''


print(3*'um'+'tyr')  # +号用来字符串连接；*表示多个重复

print('44' '678') #两个封闭的字符串 相邻，则字符串自动相连

text = ('Put several strings within parentheses '
         'to have them joined together.')
print(text)

print(text[0]) #字符串索引操作
print(text[-1]) #字符串索引操作,字符串最后一个字符

print(text[0:2]) #字符串切片
print(text[:2]) #字符串切片
print(text[2:]) #字符串切片
print(text[-12:-2]) #字符串切片

#text[0] = 'J'   #String的数据是不可变的
#print(text)
print('J'+text[1:])

print(len(text))
