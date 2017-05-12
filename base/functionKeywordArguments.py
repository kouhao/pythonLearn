'''
Created on 2017年5月11日
python funtion 关键字参数
keyword argument 意义是：传递参数是同key值来确定传递的对应的值，否则函数参数通过顺序来设定参数
@author: Administrator
'''


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):  # keyword argument
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


def cheeseshop(kind, *arguments, **keywords):  # *arguments 传的是元组；**keywords 传的是dict
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


def parrot_new(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


def make_incrementor(n):  # Lambda Expressions
    return lambda x: x + n  # 返回lambda函数


if __name__ == '__main__':
    # 1 positional argument
    parrot(1000)
    parrot(voltage=1000)                                  # 1 keyword argument
    parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
    parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
    # 3 positional arguments
    parrot('a million', 'bereft of life', 'jump')
    # 1 positional, 1 keyword
    parrot('a thousand', state='pushing up the daisies')
    print("##" * 40)
    cheeseshop("Limburger", "It's very runny, sir.",
               "It's really very, VERY runny, sir.",
               shopkeeper="Michael Palin",
               client="John Cleese",
               sketch="Cheese Shop Sketch")
    print("##" * 40)
    d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
    parrot_new(**d)
    print("##" * 40)
    f = make_incrementor(42)
    print(f(0))

    pass
