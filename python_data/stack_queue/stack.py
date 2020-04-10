#!/usr/bin/python3
# -*- coding:utf-8 -*-

'stack test'

__author__ = 'Zhang Han'

class StackUnderFlow(ValueError):   #栈下溢
    pass

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

class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LStack():
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderFlow('in pop')
        value = self._top.elem
        self._top = self._top.next
        return value

    def top(self):
        if self._top is None:
            raise StackUnderFlow('in top')
        return self._top.elem


def check_parens(text):
    parens = '()[]{}'
    open_parens = '([{'
    opposite = {')' : '(', ']' : '[', '}' : '{'}

    def find_parens(text):
        i = 0
        while i < len(text):
            if text[i] not in parens:
                i += 1
                continue
            elif text[i] in parens:
                yield text[i], i
            i += 1

    st = SStack()
    for pr, i in find_parens(text):
        if pr in open_parens:
            st.push(pr)
        elif opposite[pr] is not st.pop():
            print('Fail in ' + str(i) + ' for ' + pr)
            return False
        else:
            pass
    if st.is_empty():
        print('All complete')
        return True
    else:
        print('fault')

check_parens('((()')

import re
print(re.findall(r'\S', '3       + 2 + 1 a + 0'))
s = '3 + 2 + 1 +a 0'

print(list(filter(str.isalnum, s)))

dire = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2

def possible(maze, pos):
    return maze[pos[0]][pos[1]] == 0

def solve(maze, pos, end):
    mark(maze, pos)
    if pos == end:
        print(pos, end=' ')
        return True
    for i in range(4):
        nextp = pos[0] + dire[i][0], pos[1] + dire[i][1]
        if possible(maze, nextp):
            if solve(maze, nextp, end):
                print(pos, end=' ')
                return True
    return False

def maze_solve(maze, start, end):
    mark(maze, start)
    if start == end:
        print(start)
        return
    st = SStack()
    st.push((start, 0))
    while not st.is_empty():
        pos, nxt = st.pop()
        for i in range(nxt, 4):
            nextp = pos[0] + dire[i][0], pos[1] + dire[i][1]
            if nextp == end:
                print(nextp, end=' ')
                print(pos, end= ' ')
                while not st.is_empty():
                    print(st.pop()[0], end=' ')
                return
            if possible(maze, nextp):
                mark(maze, nextp)
                st.push((pos, i+1))
                st.push((nextp, 0))
                break





maze = [[1 for i in range(14)], [1,0,0,0,1,1,0,0,0,1,0,0,0,1], [1,0,1,0,0,0,0,1,0,1,0,1,0,1],
         [1,0,1,0,1,1,1,1,0,1,0,1,0,1], [1,0,1,0,0,0,0,0,0,1,1,1,0,1], [1,0,1,1,1,1,1,1,1,1,0,0,0,1],
         [1,0,1,0,0,0,0,0,0,0,0,1,0,1], [1,0,0,0,1,1,1,0,1,0,1,1,0,1], [1,0,1,0,1,0,1,0,1,0,1,0,0,1],
         [1,0,1,0,1,0,1,0,1,1,1,1,0,1], [1,0,1,0,0,0,1,0,0,1,0,0,0,1], [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

maze_solve(maze, (1,1), (10,12))
solve(maze, (1,1), (10,12))
