'''
Created on 2017年5月11日

@author: Administrator
'''
from collections import deque


def testQueue():  # 测试queue
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")  # Terry arrives
    queue.append("Graham")  # Graham arrives
    print(queue)
    print(queue.popleft())
    print(queue.popleft())
    print(queue)
    pass


def nestedList():  # 多重列表操作
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    a = [[row[i] for row in matrix] for i in range(4)]
    b = [[ai[i] for ai in a] for i in range(3)]
    print(a)
    print(b)
    pass


def testDel():  # del操作
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    del a[0]
    print(a)
    del a[2:4]
    print(a)
    pass


def testTuple():  # 元组，元组数据不能赋值，但是可以包含可变的对象
    t = 12345, 54321, 'hello!'
    print(t)
    u = t, (1, 2, 3, 4, 5)
    print(u)
    # u[0] = 999    #元组数据不能赋值
    v = ([1, 2, 3], [3, 2, 1])  # 可以包含可变的对象

    empty = ()
    singleton = 'hello',  # 通过这种方式生成元组
    print(len(empty))
    print(len(singleton))
    print(singleton)
    pass


def testSet():  # 用｛｝与set() 方法来创建set；同时创建空set不能用｛｝，应该用set()
    # step one
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)
    # step two
    a = set()
    a.add('apple')
    print(a)
    # step three   各个set之间的操作
    a = set('abracadabra')
    b = set('alacazam')
    print(a - b)  # letters in a but not in b
    print(a | b)  # letters in either a or b
    print(a & b)  # letters in either a and  b
    print(a ^ b)  # letters in a or b but not both
    pass


def testDict():  # 字典的key是是数字与string,是不可变的类型；tuple如果只包含String与num以及tuples,那么tuple也可以作为key;
    # 如果tuple直接包含或者间接包含可变的变量，那么是不可以作为key的；
    tel = {'jack': 4098, 'sape': 4139}
    tel['guido'] = 4127
    print(tel)
    del tel['sape']
    tel['irv'] = 4127
    print(tel)
    print(tel.keys())
    print(list(tel.keys()))
    print('guido' in tel)

    a = dict()
    print(a)
    a["4335"] = 66
    print(a)
    print(dict(sape=4139, guido=4127, jack=4098))
    print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
    pass


def testLoop():  # 循环技术
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    print(knights.items())
    for key, v in knights.items():  # 方法items() 遍历字典时，同时获取key与value
        print(key, v)

    # 方法enumerate()，将sequence数据转换程index与value
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)

    # 方法zip(),将同时遍历多个（两个或者超过两个）时
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    answers1 = ['lancelot1', 'the holy grail1', 'blue1']
    for q, a, n in zip(questions, answers, answers1):
        print('What is your {0}?  It is {1}. It is {2}. '.format(q, a, n))

    # 方法reversed()，将sequence 数据反向输出
    for i in reversed(range(1, 10, 2)):
        print(i)

    # 方法sort()，将list重新排序，renturn 返回list
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    print(sorted(set(basket)))
    for f in sorted(set(basket)):
        print(f)
    pass


def testComparing():
    # 序列对象能够与相同的序列对象进行比较；
    print((1, 2, 3) < (1, 2, 4))
    print([1, 2, 3] < [1, 2, 4])
    print('ABC' < 'C' < 'Pascal' < 'Python')
    print((1, 2, 3, 4) < (1, 2, 4))
    print((1, 2) < (1, 2, -1))
    print((1, 2, 3) == (1.0, 2.0, 3.0))
    print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))
    pass


if __name__ == '__main__':
    testQueue()
    print("**" * 40)
    nestedList()
    print("**" * 40)
    testDel()
    print("**" * 40)
    testTuple()
    print("**" * 40)
    testSet()
    print("**" * 40)
    testDict()
    print("**" * 40)
    testLoop()
    print("**" * 40)
    testComparing()
    pass
