'''
Created on 2017年5月11日
List的操作
@author: Administrator
'''

if __name__ == '__main__':
    squares = [1, 4, 9, 16, 25]  #生成list
    print(squares[0]) #list索引
    print(squares[1:3]) #list切片
    print(squares[:])   #获取list全部数据
    print(squares[:] ==squares)  #比较
    
    #将数据加入list,用append方法
    squares.append(4)
    print(squares)
    
    #list 的切片能够赋值
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(letters[2:5])
    letters[2:5] = 'Y'
    print(letters)
    pass