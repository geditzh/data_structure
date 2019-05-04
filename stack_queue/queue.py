#!usr/bin/python3
# -*- coding:utf-8 -*-

'queue test'

__author__ = 'Zhang Han'

class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class QueueUnderFlow(ValueError):
    pass

class LQueue():
    def __init__(self):
        self._peek = None
        self._blow = None

    def is_empty(self):
        return self._peek is None

    def enqueue(self, elem):
        if self._peek is None:
            self._blow = LNode(elem)
            self._peek = self._blow
            return
        self._blow.next = LNode(elem)
        self._blow = self._blow.next

    def dequeue(self):
        if self._peek is None:
            raise QueueUnderFlow('in dequeue')
        # if self._peek.next is None:
        #     value = self._peek.value
        #     self._peek = None
        #     self._blow = None
        #     return
        value = self._peek.elem
        self._peek = self._peek.next
        return value

    def peek(self):
        if self._peek is None:
            raise QueueUnderFlow('in peek')
        return self._peek.elem


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


que = LQueue()
que.enqueue(10)
que.enqueue(20)
que.dequeue()
que.dequeue()
que.enqueue(100)
print(que.dequeue())

que = SQueue()
print(que.is_empty())
que.enqueue(10000)
print(que.peek())
que.dequeue()
try:
    print(que.peek())
except Exception as e:
    print(e)
else:
    pass
finally:
    pass

