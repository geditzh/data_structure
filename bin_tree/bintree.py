#!/usr/bin/python3
# -*- coding:utf-8 -*-

__author__ = 'Zhang Han'

'bin_tree test'

class SStack():
    def __init__(self):
        self._elems = list()

    def is_empty(self):
        return self._elems == []

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderFlow('in pop')
        value = self._elems.pop()
        return value

    def top(self):
        if self._elems == []:
            raise StackUnderFlow('in top')
        return self._elems[-1]

class SQueue():
    def __init__(self, init_len=8):
        self._len = init_len
        self._elems = [0] * self._len
        self._head = 0
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if self._num == 0:
            raise QueueUnderFlow('in peek')
        return self._elems[self._head]

    def dequeue(self):
        if self._num == 0:
            raise QueueUnderFlow('in dequeue')
        value = self._elems[self._head]
        self._head = (self._head+1) % self._len
        self._num -= 1
        return value

    def enqueue(self, elem):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head+self._num) % self._len] = elem
        self._num += 1

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head+i) % old_len]
        self._elems = new_elems
        self._head = 0


def BinTree(data, left=None, right=None):
    return [data, left, right]

def is_empty_BinTree(btree):
    return btree is None

def root(btree):
    return btree[0]

def left(btree):
    return btree[1]

def right(btree):
    return btree[2]

def set_root(btree, data):
    btree[0] = data

def set_left(btree, left):
    btree[1] = left

def set_right(btree, right):
    btree[2] = right

class BinTNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def count_BinTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)

def sum_BinTNodes(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)

def print_BinTNodes(t):
    if t is None:
        print('^', end=' ')
        return
    else:
        print('(', t.data, end=' ')
        print_BinTNodes(t.left)
        print_BinTNodes(t.right)
        print(')', end=' ')


def level_print(t):
    qu = SQueue()
    qu.enqueue(t)
    while not qu.is_empty():
        t = qu.dequeue()
        print(t.data)
        if t.left is not None:
            qu.enqueue(t.left)
        if t.right is not None:
            qu.enqueue(t.right)

def preorder_elems(t):
    st = SStack()
    while t is not None or not st.is_empty():
        while t is not None:
            print(t.data, end=' ')
            st.push(t.right)
            t = t.left
        t = st.pop()

def midorder_elems(t):
    st = SStack()
    while t is not None or not st.is_empty():
        while t is not None:
            st.push(t)
            t = t.left
        t = st.pop()
        print(t.data, end=' ')
        t = t.right


if __name__ == '__main__':
    t1 = BinTNode(3, BinTNode(6, BinTNode(12)), BinTNode(9))
    print(count_BinTNodes(t1))
    print(sum_BinTNodes(t1))
    print_BinTNodes(t1)
    level_print(t1)
    preorder_elems(t1)
    midorder_elems(t1)
