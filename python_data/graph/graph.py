#!/usr/bin/python3
#-*- coding:utf-8 -*-

__author__ = "Zhang Han"

class Graph():
    def __init__(self, mat, uncon=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError('in init')
        self._mat = [mat[i][:] for i in range(vnum)]
        self._uncon = uncon
        self._vnum = vnum

    def vertex_num(self):
        return self._vnum

    def invalid(self, v):
        return v < 0 or v >= self._vnum

    def add_edge(self, vi, vj, val=1):
        if self.invalid(vi) and self.invalid(vj):
            raise ValueError('in add_edge')
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self.invalid(vi) or self.invalid(vj):
            raise ValueError('in get_edge')
        return self._mat[vi][vj]

    def out_edge(self, vi):
        if self.invalid(vi):
            raise ValueError('in out_edge')
        return self._out_edge(self._mat[vi], self._uncon)

    @staticmethod
    def _out_edge(row, uncon):
        edge = []
        for i in range(len(row)):
            if row[i] != uncon:
                edge.append((i, row[i]))
        return edge

class GraphAL(Graph):
    def __init__(self, mat=[], uncon=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError('in init')
        self._mat = [Graph._out_edge(mat[i], uncon) for i in range(vnum)]
        self._vnum = vnum
        self._uncon = uncon

    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0 or self.invalid(vi) or self.invalid(vj):
            raise ValueError('in add_edge')

        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i] = (vj, val)
            if row[i][0] > vj:
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        if self.invalid(vi) or self.invalid(vj):
            raise ValueError('in get_edge')
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._uncon

    def out_edge(self, vi):
        if self.invalid(vi):
            raise ValueError('in out_edge')
        return self._mat[vi]




