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

# from functools import reduce

# def square(n):
#     for key,value in enumerate(n):
#         n[key] = value**2
#     return n

# def main():
#     a = [1,2,3,4,5,5]
#     print(square(a))
#     print(reduce(lambda x, y : x * 10 + y, a))


# if __name__ == '__main__':
#     main(0010# import sys
# def test():
#     print(sys.thread_info)

# def main():
#     f = test
#     f()
#     print(f.__name__)
#     print(int('100', base=2))

# if __name__ == '__main__':
#     main()abc

# from functools import partial

# max2 = partial(max, 10)
# print(max2(*[1,2,3,4,5]))

# class Student():

#     def __init__(self, name, score, age=24,):
#         self.name = name
#         self.age = age
#         self.score = score

#     def show_info(self):
#         print(self.name + ': ' + "age: " + str(self.age) + " score: " + str(self.score))

# def main():
#     stu1 = Student("zhanghan", 90)
#     stu2 = Student("zhouyi", 95, age=18)
#     stu1.show_info()
#     stu2.show_info()

#     a = [1,5,6,8]
#     b = [5,6,7,9]
#     a.extend(b)

#     cnt = 5
#     a = [0 for x in range(cnt)]
#     print(a)


# if __name__ == '__main__':
# #     main()
# class Solution:
#     def __init__(self):
#         pass
#     def moveZeroes(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         cnt = []
#         for key, value in enumerate(nums):
#             if  nums[key] == 0:
#                 cnt.append(key)
#         for i in range(len(cnt)):
#             nums.remove(0)
#         nums.extend([0 for i in range(len(cnt))])
#         return nums

# s = Solution()
# s = s.moveZeroes([0,0,5])
# # print(s)

# # for i in range(5):
# #     print(i)
# #     i += 2

# input = '19+3-19+18='
# a = list(range(10))
# for i in range(len(a)):
#     a[i] = str(a[i])

# num = []
# fox = []
# s = ''
# for value in input:
#     if value not in a:
#         num.append(s)
#         fox.append(value)
#         s = ''
#     else:
#         s += value

# print(num)
# print(fox)
# sum = int(num[0])

# for i in range(len(num)-1):
#     fox_res = fox.pop(0)
#     if fox_res == '+':
#         sum += int(num[i+1])
#     elif fox_res == '-':
#         sum -=  int(num[i+1])

# print(sum)

# class Student():
#     '''a test for class'''
#     def __init__(self, name, age):
#         self._name = name
#         self.age = age

#     def print_info(self):
#         print('name is : ' + self._name + "\nage is : " + str(self.age))

# class Stud(Student):
#     '''a sub class'''
#     def __init__(self, name, age, score):
#         super().__init__(name, age)
#         self._score = score

#     def print_info(self):
#         print('name is : ' + self._name + '\nscore is : ' + str(self._score) + '\nage is : ' + str(self.age))

# def test(s):
#     s.print_info()

# if __name__ == '__main__':
#     stu1 = Student("zhanghan", 25)
#     test(stu1)
#     stu2 = Stud("zhouyi", 21, 90)
#     test(stu2)
#     print(stu2._score)


#     a = 10/0
# except Exception as e:
#     raise Fooerror('mather')
# else:
#     print('no error')
# finally:
#     print('finish')
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n

# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
#     else:
#         print('no error')
#     finally:
#         print('finally')
# bar()

# def fib(n):
#     f1 = f2 = 1
# #     for i in range(1, n):
# #         f1, f2 = f2, f1 + f2
# #     return f2

# # print(fib(3))
# a = [0 for i in range(26)]
# print(len(a))
# a = list(map(str, a))
# print(a)

# print(chr(ord('A') + 32))
# a = {1,2,3,4,5}
# if 3 in a:
#     print('zz')


# print(0 and 0)

# a = {"1":2, "2":3}
# for key in a.keys():
#     value = 3-int(key)
#     print(int(key))
def twoSum(nums, target):
    a = dict()
    if nums == []:
        return None
    for i, value in enumerate(nums):
        if value >= target:
            continue
        a[value] = i

    for key in a.keys():
        temp = target - key
        if temp in a:
            return [a[key], a[target-key]]


# b = twoSum([3,2,4], 6)
# print(b)

# a = 'zz'
# b = 'zz'
# if a == b:
#     print(123)
# i = 0
# for column in range(i//3*3,(i//3+1)*3):
#     for row in range(i//3*3,(i//3+1)*3):
#         print(row, column)
# a = [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11],
#    [16, 7,10,11]
# ]
# print(len(a[0]))
# a  = [1,2,3,4,5,6,7]
# print(a[3::-1])

# import time
# start = time.clock()
# a = [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11],
#    [16, 7,10,11]
# ]
# print(len(a[0]))
# a  = [1,2,3,4,5,6,7]
# print(a[3::-1])
# end = time.clock()
# # print(end-start)
# import time

# a = [i for i in range(1000000)]
# b = list(map(str,a))
# d = {x:y for x,y in zip(a,b)}

# start = time.time()
# 999 in a
# end = time.time()
# print(end-start)

# start = time.clock()
# 999 in d
# end = time.clock()
# print(end-start)

# s = {123,345,123,456}
# s.remove(123)
# print(s)

# s = ["h","e","l","l",'3']
# s = s[::-1]

# a = ''
# for i in range(len(s)):
#     a += s[i]

# print(a)

# a = {1,2,3,4,5}
# b = {3,4,5,6,7}
# a = [123]
# print(a.extend([1,2,3,5,6]))
# b = [1,2,3,4,5,6]
# a = a+b
# print(a)

# a = 123
# print(list(str(a)))

# def reverse(x):
#     l = list(str(x))
#     l = l[::-1]
#     if l[-1] == '-':
#         l.pop()
#         l.insert(0, '-')
#     s = ''
#     for value in l:
#         s += value
#     return int(s)

# print(reverse(123))

# def reverse(x):
#     i, j = 0, len(x)-1
#     while i < j:
#         x[i], x[j] = x[j], x[i]
#         i +=1
#         j -=1
#     return x

# a = [1,2,3,4,5]
# print(reverse(a))

# def myAtoi(str):
#     str = str.lstrip()
#     if str[0] > '9' or str[0] < '0':
#         if str[0] != '-':
#             return 0

#     i = 0
#     while i < len(str):
#         if str[i] == '-':
#             i += 1
#             continue
#         if str[i] > '9' or str[i] < '0':
#             str = str[:i]
#             break
#         i += 1
#     return int(str)

# print(myAtoi(" -4444 w"))
# print(INT_MAX)

a = ['123\n','456\n','789\n']
with open('a.txt', 'w') as f:
        f.writelines(a)

with open('a.txt', 'r') as f:
    print(f.readlines())

# import os
# print(os.environ)

# import re
# a = 'C:\\uer\\bin'
# print(a)
# b = '010-1111111'
# print(b)

# print(re.findall(r"\bI","IMISS IOU"))

# a = '122343243+456-789'
# print(re.findall(r'\d+|\W', a))

# a = '123-123412345'
# print(re.findall(r'12345*', a))

# def list_sort(lst):
#     for i in range(1,len(lst)):
#         x = lst[i]
#         j = i
#         while j > 0 and lst[j-1] > x:
#             lst[j] = lst[j-1]
#             j -= 1
#         lst[j] = x
#     return lst

# a = [5,54,4,6,7,8,6,4,2,5]
# print(list_sort(a))

# def josephus(n, k, m):
#     person = list(range(1, n+1))
#     i = k - 1
#     for num in range(n):
#         count = 0
#         while count < m:
#             if person[i] > 0:
#                 count += 1
#             if count == m:
#                 print(person[i], end='')
#                 person[i] = 0
#             i = (i+1) % n
#         if num < n - 1:
#             print(', ', end='')
#         else:
#             print('')
# def josephus1(n, k, m):
#     person = list(range(1, n+1))
#     num, i = n, k-1
#     for num in range(n, 0, -1):
#         i = (i+m-1) %  num
#         print(person.pop(i), end=(', ' if num > 1 else '\n'))



# josephus(10,2,7)
# josephus1(10,2,7)

# for i in range(0):
#     print(i)

# a = '123412341234,1234,1234+2134,2314,1234'
# print(a.find('1234+'))


# import re

# pattern = re.compile(r'(abc.) (abc.)')

# print(re.finditer(pattern, 'abcd abcz'))
# for n in re.finditer(pattern, 'abcd abcg abct abcf'):
#     print(n.group())

# a = 'z23'
# print(ord(a[0]))

# a = 'A man, a plan, a canal: Panama'
# p = re.findall(r'\w', a.lower())
# print(p)
# s = list(filter(str.isalnum, a.lower()))
# print(s)
# def calc_num(weight, wlist, n):
#     if weight == 0:
#         return True
#     if weight < 0 or (weight >0 and n<1):
#         return False
#     if calc_num(weight-wlist[n-1], wlist, n-1):
#         print('subnum is '+ str(n) +str(wlist[n-1]))
#         return True
#     if calc_num(weight, wlist, n-1):
#         return True
#     else: return False

# a = [1,2,3,4,5,6,7,8,9,10]
# calc_num(20, a, 8)

# def knap_rec(weight, wlist, n, a):
#     if weight < 0 or (weight > 0 and n < 1):
#         return False
#     if weight == 0:
#         return True
#     if knap_rec(weight, wlist , n-1, a):
#         return True
#     if knap_rec(weight - wlist[n-1], wlist, n-1, a):
#         a.append(wlist[n-1])
#         print('items is : ' , wlist[n-1], n-1)
#         return True
#     else:return False

# a = list()
# knap_rec(20, [1,2,4,5,6,7,9,10], 9, a)
# print(a)

# class SStack():
#     def __init__(self):
#         self._elems = list()

#     def is_empty(self):
#         return self._elems == []

#     def push(self, *elem):
#         self._elems.append(elem)

#     def pop(self):
#         if self._elems == []:
#             raise StackUnderFlow('in pop')
#         value = self._elems.pop()
#         return value

#     def top(self):
#         if self._elems == []:
#             raise StackUnderFlow('in top')
#         return self._elems[-1]


# dire = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# def mark(maze, pos):
#     maze[pos[0]][pos[1]] = 2

# def possible(maze, pos):
#     return maze[pos[0]][pos[1]] == 0

# def solve(maze, pos, end):
#     mark(maze, pos)
#     if pos == end:
#         print(pos, end=' ')
#         return True
#     for i in range(4):
#         nextp = pos[0] + dire[i][0], pos[1] + dire[i][1]
#         if possible(maze, nextp):
#             if solve(maze, nextp, end):
#                 print(pos, end=' ')
#                 return True
#     return False

# def maze_solve(maze, start, end):
#     mark(maze, start)
#     if start == end:
#         print(start)
#         return
#     st = SStack()
#     st.push(start, 0)
#     while not st.is_empty():
#         pos, nxt = st.pop()
#         for i in range(nxt, 4):
#             nextp = pos[0] + dire[i][0], pos[1] + dire[i][1]
#             if nextp == end:
#                 print(nextp, end=' ')
#                 print(pos, end= ' ')
#                 while not st.is_empty():
#                     print(st.pop()[0], end=' ')
#                 return
#             if possible(maze, nextp):
#                 mark(maze, nextp)
#                 st.push(pos, i+1)
#                 st.push(nextp, 0)
#                 break





# maze = [[1 for i in range(14)], [1,0,0,0,1,1,0,0,0,1,0,0,0,1], [1,0,1,0,0,0,0,1,0,1,0,1,0,1],
#          [1,0,1,0,1,1,1,1,0,1,0,1,0,1], [1,0,1,0,0,0,0,0,0,1,1,1,0,1], [1,0,1,1,1,1,1,1,1,1,0,0,0,1],
#          [1,0,1,0,0,0,0,0,0,0,0,1,0,1], [1,0,0,0,1,1,1,0,1,0,1,1,0,1], [1,0,1,0,1,0,1,0,1,0,1,0,0,1],
#          [1,0,1,0,1,0,1,0,1,1,1,1,0,1], [1,0,1,0,0,0,1,0,0,1,0,0,0,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

# maze_solve(maze, (1,1), (10,12))
# solve(maze, (1,1), (10,12))

# import re, operator

# a = '1+2-456-345=33'
# b = a.strip()
# b = re.findall(r'\d+|\+|\-|\=', b)
# print(b)

# def bssearch(lst, key):
#     low, high = 0, len(lst) - 1
#     while low <= high:
#         mid = low + (high - low) // 2
#         if lst[mid] == key:
#             return lst[mid]
#         if lst[mid] < key:
#             low = mid + 1
#         else:
#             high = mid - 1
#         print(low, end=' ' )
#         print(mid, end=' ')
#         print(high)
#     return None

# a = [1,2,3,4,5,6,7,8,9,10]
# print(bssearch(a, 2))

# class Assoc(object):
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value

#     def __lt__(self, other):
#         return self.key < other.key

#     def __le__(self, other):
#         return self.key <= other.key

#     def __str__(self):
#         return 'Asscos({0}, {1})'.format(self.key, self.value)

# x = Assoc(7,100)
# y = Assoc(9,200)
# z = Assoc(5,300)
# lst = [x, y, z]
# lst.sort()
# print(str(lst[0]))
# print(len(lst))

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = s.replace(' ', '%20')
        return s

if __name__ == '__main__':
    try:
        solu = Solution()
        s = input()
        print(solu.repacceSpace(s))
    except:
        pass
# def sss(lst):
#     j, n = 1, len(lst)
#     for j in range(1, n):
#         i = j
#         while i > 0 and lst[i-1] > lst[i]:
#             lst[i-1], lst[i] = lst[i], lst[i-1]
#             i -= 1
#     return lst

# b = [1,3,5,8,5,3,65,8,0,8,7]
# print(sss(b))
# print(pow(256, 10))

# def intersection(a, b):
#     i, j = 0, 0
#     res = []
#     while i<len(a) and j < len(b):
#         if a[i] < b[j]:
#             i += 1
#         elif a[i] > b[j]:
#             j += 1
#         else:
#             res.append(a[i])
#             i += 1
#             j += 1
#     return res


# a = [1,2,3,4,5,6,6,7]
# b = [1,3,5,7]
# print(intersection(a, b))

# print(hash('a'))
# print(hash('a'))
# print('sadf'.replace('s', 'A'))
# print(dir(str))


