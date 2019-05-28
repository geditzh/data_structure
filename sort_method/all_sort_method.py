#!/usr/bin/python3
# -*-coding:utf-8 -*-

__author__ = 'Zhang Han'

'all sort methods'

class record(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __lt__(self, other):
        return self.key < other.key
    def __le__(self, other):
        return self.key <= other.key

def insert_method(lst):
    for i in range(1, len(lst)):
        j = i
        x = lst[i]
        while j > 0 and lst[j-1] > x:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = x
    return lst

def select_method(lst):
    for i in range(0, len(lst)-1):
        x = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[x]:
                x = j
        if x != i:
            lst[i], lst[x] = lst[x], lst[i]
    return lst

def heap_method(lst):
    def siftdown(lst, e, begin, end):
        i, j = begin, begin*2+1
        while j < end:
            if j+1 < end and lst[j+1] < lst[j]:
                j += 1
            if lst[j] > e:
                break
            lst[i] = lst[j]
            i, j = j, 2 * j + 1
        lst[i] = e

    end = len(lst)
    for i in range(end//2-1, -1, -1):
        siftdown(lst, lst[i], i, end)
    for i in range(end-1, 0, -1):
        e = lst[i]
        lst[i] = lst[0]
        siftdown(lst, e, 0, i)
    return lst

def bubble_method(lst):
    for i in range(len(lst)-1):
        found = False
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                found = True
        if not found:
            break
    return lst

def quick_sort(lst):
    def qsort_method(lst, begin, end):
        if begin >= end:
            return
        i = begin
        j = end
        dummy = lst[i]
        while i < j:
            while i < j and lst[j] > dummy:
                j -= 1
            if i < j:
                lst[i] = lst[j]
                i += 1
            while i < j and lst[i] < dummy:
                i += 1
            if i < j:
                lst[j] = lst[i]
                j -= 1
        lst[i] = dummy
        qsort_method(lst, begin, i-1)
        qsort_method(lst, i+1, end)

    qsort_method(lst, 0, len(lst)-1)
    return lst



def main():
    a = [5,0,1,8,3,7,4,6]
    b = []
    for x in a:
        b.append(record(x, x))
    for i in quick_sort(b[:]):
        print(i.value, end='')
    for i in b:
        print(i.value, end='')

if __name__ == '__main__':
    main()
