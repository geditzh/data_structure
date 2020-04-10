#!/usr/bin/python3
# -*-conding:utf-8 -*-

__author__ = 'Zhang Han'

'binary tree to achieve dict'

from dict_bin_tree import BinTNode, DictBinTree

class AVLNode(BinTNode):
    def __init__(self, data):
        super().__init__(data)
        self.bf = 0

class Assoc(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __str__(self):
        return 'Assoc is {0}, {1}'.format(self.key, self.value)

class DictAVL(DictBinTree):
    def __init__(self):
        super().__init__()

    @staticmethod
    def LL(a, b):
        a.left = b.right
        b.right = a
        b.bf, a.bf = 0, 0
        return b

    @staticmethod
    def RR(a, b):
        a.right = b.left
        b.left = a
        b.bf = a.bf = 0
        return b

    @staticmethod
    def LR(a, b):
        c = b.right
        b.right, a.left = c.left, c.right
        c.right, c.left = a, b
        if c.bf == 0:
            a.bf = b.bf = 0
        elif c.bf == 1:
            b.bf = 0
            a.bf = -1
        else:
            a.bf = 0
            b.bf = 1
        c.bf = 0
        return c

    @staticmethod
    def RL(a, b):
        c = b.left
        a.right, b.left = c.left, c.right
        c.left, c.right = a, b
        if c.bf == 0:
            a.bf = b.bf = 0
        elif c.bf == 1:
            a.bf = 0
            b.bf = -1
        else:
            b.bf = 0
            a.bf = 1
        c.bf = 0
        return c

    def insert(self, key, value):
        a = p = self._root
        if a is None:
            self._root = AVLNode(Assoc(key, value))
            return
        pa = q = None
        while p is not None:
            if p.data.key == key:
                p.data.value = value
                return
            if p.bf != 0:
                pa, a = q, p
            q = p
            if key < p.data.key:
                p = p.left
            else:
                p = p.right
        node = AVLNode(Assoc(key, value))
        if key > q.data.key:
            q.right = node
        else:
            q.left = node
        if key < a.data.key:
            p = b = a.left
            d = 1
        else:
            p = b = a.right
            d = -1
        while p != node:
            if key < b.data.key:
                b.bf = 1
                p = p.left
            else:
                b.bf = -1
                p = p.right
        if a.bf == 0:
            a.bf = d
            return
        if a.bf == -d:
            a.bf = 0
            return
        if d == 1:
            if b.bf == 1:
                b = DictAVL.LL(a, b)
            else:
                b = DictAVL.LR(a, b)
        else:
            if b. bf == -1:
                b = DictAVL.RR(a, b)
            else:
                b = DictAVL.RL(a, b)
        if pa is None:
            self._root = b
        else:
            if pa.left == a:
                pa.left = b
            else:
                pa.right = b






