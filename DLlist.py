#!/usr/bin/python3
# -*- coding:utf-8 -*-

'studing date structure'

__author__ = 'Zhang Han'

from Llist import LNode, LList_b, LinkedListUnderFlow

class DLNode(LNode):
    def __init__(self, elem, prev=None, next_=None):
        super().__init__(elem, next_)
        self.prev = prev

class DLList_b(LList_b):
    def __init__(self):
        super().__init__()

    def prepend(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderFlow('in pop')
        value = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return value

    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderFlow('in pop_last')
        value = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is not None:
            self._rear.next = None
        else:
            self._head = None
        return value

    def reverse(self):
        if self._head is None:
            return
        p, q = self._head, self._rear
        while p is not q:
            p.elem, q.elem = q.elem, p.elem
            p = p.next
            q = q.prev


dllist = DLList_b()
for i in range(11):
    dllist.append(i)
dllist.printall()
dllist.reverse()
dllist.printall()
