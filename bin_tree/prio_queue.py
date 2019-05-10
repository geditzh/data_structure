#!/usr/bin/python3
# -*- coding:utf-8 -*-

__author__ = 'Zhang Han'

'bin_tree test'

class PriorityQueueError(ValueError):
    pass

class PrioQueue(object):
    '''用堆来实现最优序列'''
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if len(self._elems) > 0:
            self.bulid_heap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PriorityQueueError('in peek')
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)
    def siftup(self, e, end):
        elems, i, j = self._elems, end, (end - 1) // 2
        while j >= 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PriorityQueueError('in dequeue')
        e0 = self._elems[0]
        e = self._elems.pop()
        if len(self._elems) > 0:
            self.siftdown(e, 0, len(self._elems))
        return e0
    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, 2 * begin + 1
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, j * 2 + 1
        elems[i] = e

    def bulid_heap(self):
        end = len(self._elems)
        for i in range(end//2-1, -1, -1):
            self.siftdown(self._elems[i], i, end)

def heap_sort(elems):
    def siftdown(elems, e, begin, end):
        i, j = begin, 2*begin+1
        while j < end:
            if j+1 < end and elems[j+1] > elems[j]:
                j +=1
            if e > elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j+1
        elems[i] = e

    end = len(elems)
    for i in range(end//2-1, -1, -1):
        siftdown(elems, elems[i], i, end)
    for i in range(end-1, -1, -1):
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e, 0, i)
    return elems

a = [3,4,6,7,4,2,4,7,9,0,8,6,5,3,2,1,1,11,2223,45555]
print(heap_sort(a))


# pq = PrioQueue([5,9,7,8,6,3,4,1010,-5,10])
# print(pq._elems)
# pq.dequeue()
# print(pq._elems)
# pq.dequeue()
# print(pq._elems)
# pq.dequeue()
# print(pq._elems)
# pq.dequeue()
# print(pq._elems)
# pq.dequeue()
# print(pq._elems)
# pq.dequeue()
# print(pq._elems)
# pq.dequeue()
# print(pq._elems)
# pq.dequeue()
# print(pq._elems)
# pq.dequeue()
# print(pq._elems)
# pq.dequeue()
# print(pq._elems)

