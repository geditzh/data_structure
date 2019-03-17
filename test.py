#!/usr/bin/python3
# -*- utf-8 -*-

'a test model'

__author__ = 'Zhang Han'

# print('zhanghan')

# print('zh')
# '''
# name1 = 'zhang ' + 'han'
# name2 = ['zhouyi']
# name2.insert(-1,'hangsanfeng')
# print(name1.title(),'123')
# name2.sort()
# print(name2)

# a = [1,2,3,4 ,2,3,4,5]
# print(a)
# a = [[0 for i in range(6)] for j in range(5)]
# a[4][0]=12
# print(a)
# print(len(a))
# print(a.count(0))

# a = "zhanghan"
# a = a + '2'
# print(a)

# a  = [1,2,3,4]
# a = a+[5,6,7]
# print(a)

# a = [[value**2 for value in range(10)] for i in range(4)]
# print(a[3])
# a = [1,2,3,4,4,4,4,4,4,1,2,5,7]
# print(a)
# del a[-1]
# print(a)

# a = [0,1]
# i=2
# while i<10:
#     b = a[i-1]+a[i-2]
#     a.append(b)
#     i=i+1
# print(a)

# def show_print(first,*last,info):
#     print('fitst =',first,'last = ',last)
#     print(last[3])
#     print(b["zhanghan"])

# a = [1,2,3,4,5,6]
# b = {'zhanghan':123,"zhouyi":456}
# show_print(11,*a,b)
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     numbers[0] = 2000
#     print(numbers)
#     return sum

# num = [1,2,3,4,5]
# a = calc(num[:])
# print(num)

# def fact(num):
#     if num == 1:
#         return 1
#     else:
#         res = num*fact(num-1)
#         return res


# def fact1(num):
#     res = num
#     while num>1:
#         res = res *(num-1)
#         num = num-1
#     return res
# print(fact1(5))

# def move(n,a,b,c):
#     if n==1:
#         print(a,'-->',c)
#     else:
#         move(n-1,a,c,b)
#         move(1,a,b,c)
#         move(n-1,b,a,c)


# move(3,'a','b','c')
# a = "zhzhzh"
# print(a[0])

# from collections import Iterable as it
# print(isinstance('abc',it))

# for key,value in enumerate(['a','b','c']):
#     print(key,value)


# a = [x+y for x in "123" for y in "456"]

# # for n,value in enumerate(a):
# #     a[n] = int(a[n])
# n=0
# for value in a:
#     a[n] = int(value)
#     n=n+1

# print(a)

# a  = ['zhanghan', 'zhouyi', 18,'caonima']
# b = []

# for value in a:
#     if isinstance(value,str):
#         print(value.title())
#         b.append(value)
#     else:
#         b.append(value)
# print(b)

# b = set(b)

# print(b)

# a = (11,22,11,55)
# print(a[0])

# def fib(max):
#     n,a,b = 0,0,1
#     while n<max:
#         yield(b)
#         a,b = b,a+b
#         n=n+1
#     return "finish"

# g  = fib(6)
# while True:
#     try:
#         o  =next(g)
#         print(o)
#     except StopIteration as e:
#         print(e.value)
#         break
#     else:
#         print('zhzhzh')
#     finally:
#         print("yeah")

# def triangles(n):
#     L = [1]
#     for j in range(n):
#         yield L
#         L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]



def triangles(n):
    L = [1]
    for i in range(n):
        yield L
        add = []
        for i in range(len(L)-1):
            result = L[i]+L[i+1]
            add.append(result)
        L = [1] + add + [1]


def triangle(n):
    L = [1]
    for i in range(n):
        yield L
        add = []
        for j in range(len(L)-1):
            result = L[j]+L[j+1]
            add.append(result)
        L = [2*(i+1)+1] + add + [2*(i+1) +1]

def main():
    for i in triangle(8):
        print(i)


# if __name__ == '__main__':
#     main()

# import functools as fs

# def str2int(s):
#     def char2num(s):
#         x = [x for x in range(10)]
#         y = list(map(str,x))
#         z = {x:y for x,y in zip(y,x)}
#         return z[s]
#     return fs.reduce(lambda x,y:x*10+y,map(char2num,s))

# print(str2int('1255534'))

# def not_empty(s):
#     return s and s.strip()

# print(list(filter(not_empty,['s','b','',' ',None])))

def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

def _isdivisibal(n):
    return lambda x : x%n>0

def primes(n):
    if n == 0:
        return None
    yield 2
    it = _odd_iter()
    for i in range(n-1):
        o = next(it)
        yield o
        it = filter(_isdivisibal(o),it)
    return 'done'

def issame(n):
    s = str(n)
    for x in range(int(len(s)/2)+1):
        if s[x] != s[-1-x]:
            return False
        else:
            return True

# print(list(filter(issame,range(1000))))


# def is_same(n):
#     return str(n) == str(n)[::-1]

# print(list(filter(is_same,range(1000))))

a = [1,6,36,666,5,3,2,2]

print(sorted(a,reverse = True))

a = [X+Y for X in 'ABC' for Y in "XYZ"]
a = {x:y for x,y in zip("123",[4,5,6])}
print(a)
