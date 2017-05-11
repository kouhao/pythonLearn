'''
Created on 2017年5月11日
if 用法
@author: Administrator
'''

if __name__ == '__main__':
    d = int(input("please enter an integer:"))   # input 交互命令
    if d<0:
        print('Negative changed to zero')
    elif d==0:
        print('Zero')
    elif d ==1:
        print('Single')
    else:
        print('More')
    pass