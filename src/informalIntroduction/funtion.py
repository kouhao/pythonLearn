'''
Created on 2017年5月11日
定义函数
@author: Administrator
'''
def fib(n):
    a,b =0,1
    while a<n:
        print(a,end=' ')
        a,b = b, a+b
    print('g')
    
if __name__ == "__main__":
    fib(30)
    g = fib #函数能够赋值
    g(50)
    pass