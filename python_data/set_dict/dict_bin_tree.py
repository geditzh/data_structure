#!/usr/bin/python3
# -*-conding:utf-8 -*-

__author__ = 'Zhang Han'

'binary tree to achieve dict'

class BinTNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right=right

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

class DictBinTree(object):
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if entry.key > key:
                bt = bt.left
            elif entry.key < key:
                bt = bt.right
            else:
                return entry.value
        return None

    def insert(self, key,  value):
        bt = self._root
        if bt is None:
            self._root = BinTNode(Assoc(key, value))
            return
        while True:
            entry = bt.data
            if entry.key < key:
                if bt.right is None:
                    bt.right = BinTNode(Assoc(key, value))
                    return
                bt = bt.right
            elif entry.key > key:
                if bt.left is None:
                    bt.left = BinTNode(Assoc(key, value))
                    return
                bt = bt.left
            else:
                bt.data.value = value
                return

    def delete(self, key):
        p, q = None, self._root
        while q is not None and q.data.key != key:
            p = q
            if q.data.key > key:
                q = q.left
            else:
                q = q.right
        if q is None:
            return
        if q.left is None:
            if p is None:
                self._root = q.right
            elif p.left == q:
                p.left = q.right
            else:
                p.right = q.tight
            return
        r = q.left
        while r.right is not None:
            r = r.right
        r.right = q.right
        if p is None:
            self._root = q.left
        elif p.left == q:
            p.left = q.left
        else:
            p.right = q.left


    def values(self):
        st, t = [], self._root
        while t is not None or st:
            while t is not None:
                st.append(t)
                t = t.left
            t = st.pop()
            yield t.data.key,t.data.value
            t = t.right

def main():
    a = DictBinTree()
    x = (i for i in range(10))
    y = (i**2 for i in range(10))

    for i, j in zip(x,y):
        a.insert(i, j)

    for i in a.values():
        print(i)

if __name__ == '__main__':
    main()
