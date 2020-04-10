#!/usr/bin/python3
# -*- coding:utf-8 -*-

__author__ = 'Zhang Han'

'bin_tree test'

from bintree import SStack, SQueue

class BinTreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinTree():
    def __init__(self, root=None):
        self._root = root

    def is_empty(self):
        return self._root == None

    def count_BinTreeNode(self, bintnode):
        t = bintnode
        if t is None:
            return 0
        else:
            return 1 + self.count_BinTreeNode(t.left) + self.count_BinTreeNode(t.right)

    def sum_BinTreeNode(self, bintnode):
        t = bintnode
        if t is None:
            return 0
        else:
            return t.data + self.sum_BinTreeNode(t.left) + self.sum_BinTreeNode(t.right)

    def depth_BinTreeNode(self, bintnode):
        t = bintnode
        if t is None:
            return 0
        else:
            left_depth = self.depth_BinTreeNode(t.left)
            right_depth = self.depth_BinTreeNode(t.right)
            return max(left_depth, right_depth) + 1

    def level_order(self):
        qu = SQueue()
        qu.enqueue(self._root)
        while not qu.is_empty():
            t = qu.dequeue()
            print(t.data, end=' ')
            if t.left is not None:
                qu.enqueue(t.left)
            if t.right is not None:
                qu.enqueue(t.right)
        print('')

    def pre_order(self):
        st = SStack()
        t = self._root
        while t is not None or not st.is_empty():
            while t is not None:
                print(t.data, end=' ')
                st.push(t.right)
                t = t.left
            t = st.pop()
        print(' ')

    def min_order(self):
        st = SStack()
        t = self._root
        while t is not None or not st.is_empty():
            while t is not None:
                st.push(t)
                t = t.left
            t = st.pop()
            print(t.data, end=' ')
            t = t.right
        print(' ')

    def post_order(self, bintnode):
        t = bintnode
        if t is None:
            return
        else:
            self.post_order(t.left)
            self.post_order(t.right)
            print(t.data, end=' ')


a = BinTreeNode(2, BinTreeNode(4, BinTreeNode(6), BinTreeNode(8)), BinTreeNode(10))
b = BinTree(a)
print(b.count_BinTreeNode(a))
print(b.sum_BinTreeNode(a))
b.level_order()
print(b.depth_BinTreeNode(a))
b.pre_order()
b.min_order()
b.post_order(a)
