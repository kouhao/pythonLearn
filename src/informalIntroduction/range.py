'''
Created on 2017年5月11日
遍历序列的数字
@author: Administrator
'''

if __name__ == '__main__':
    for i in range(5):
        print(1,i)
        
    for i in range(3,10):  #遍历数字的范围
        print(2,i)
        
    for i in range(0, 10, 3): #遍历数字范围，以及按照特定值变化
        print(3,i)
    
    b = list(range(20,30,2)) #将range值转化为list
    print(b)
    
    #break 跳出当前for循环
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
            
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')
    
    #continue 跳出当前for的当次循环      
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found a number", num)
    #pass  什么动作也没有    
    pass