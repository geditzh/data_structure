#!/usr/bin/python3
# -*- coding:utf-8 -*-

'studing date structure'

__author__ = 'Zhang Han'

class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LinkedListUnderFlow(ValueError):
    pass

def big_than_5(elem):
    return elem > 5

class LList():
    def __init__(self):
        '''初始化'''
        self._head = None

    def is_empty(self):
        '''判空'''
        return self._head is None

    def prepend(self, elem):
        '''添加第一个元素'''
        self._head = LNode(elem, self._head)

    def pop(self):
        '''弹出第一个元素'''
        if self._head is None:
            raise LinkedListUnderFlow('in pop')
        value = self._head.elem
        self._head = self._head.next
        return value

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderFlow("in pop_last")
        if self._head.next is None:
            value = self._head.elem
            self._head = None
            return value
        p = self._head
        while p.next.next is not None:
            p = p.next
        value = p.next.elem
        p.next = None
        return value

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ',  end='')
            p = p.next
        print('')

    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def reverse(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = self._head.next
            q.next = p
            p = q
        self._head = p

    def sort(self):
        if self._head is None:
            return
        crt = self._head.next
        while crt is not None:
            x = crt.elem
            p = self._head
            while p is not crt and p.elem <= x:
                p = p.next
            while p is not crt:
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            crt.elem = x
            crt = crt.next

class LList_b(LList):
    def __init__(self):
        super().__init__()
        self._rear = None

    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderFlow('in pop_last')
        p = self._head
        if p.next is None:
            value = p.value
            self._head = None
            return value
        while p.next.next is not None:
            p = p.next
        value = p.next.elem
        p.next = None
        self._rear = p
        return value


def main():
    import random
    llist_b = LList_b()
    llist_b.prepend(99)

    for i in range(11,20):
        llist_b.append(random.randint(1,20))
    llist_b.printall()
    llist_b.reverse()
    llist_b.printall()
    llist_b.sort()
    llist_b.printall()

if __name__ == '__main__':
    main()
