'''
Created on 2017年5月11日
定义函数
@author: Administrator
'''


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print('g')


# Default Argument Values 默认参数值
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = (prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
    pass


def test(a, L=[]):  # 验证函数默认值不能为可变的值
    L.append(a)
    print(L)
    return L


def test2(a, L=None):  # 返回可变变量的修改
    if L is None:
        L = []
    L.append(a)
    print(L)
    return L


if __name__ == "__main__":
    # fib(30)
    # g = fib  # 函数能够赋值
    # g(50)
    # ask_ok('123')   #函数默认值
    test(3)   # 函数默认值应该是不可变的值
    test(4)
    test2(3)
    test2(4)
    pass
