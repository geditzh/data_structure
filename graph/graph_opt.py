#!/usr/bin/python3
# -*- coding:utf-8 -*-

'author = Zhang Han'

class Node():
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def __str__(self):
        return self.name

class Edge():
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def get_source(self):
        return self.src
    def get_destination(self):
        return self.dest
    def __str__(self):
        return self.src.get_name() + '->' + self.dest.get_name()

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        self.src = src
        self.dest = dest
        self.weight = weight
    def get_weight(self):
        return self.weight
    def __str__(self):
        return self.src.get_name() + '->' + self.dest.get_name() + ': ' + str(self.weight)

class Digraph():
    def __init__(self):
        self.node = []
        self.edge = {}
    def add_node(self, node):
        if node in self.node:
            raise ValueError('Duplicate Node')
        else:
            self.node.append(node)
            self.edge[node] = []
    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.node and dest in self.node):
            raise ValueError('in add_edge')
        self.edge[src].append(dest)
    def children_of(self, node):
        return self.edge[node]
    def has_node(self.node):
        return node in self.node
    def __str__(self):
        result = ''
        for src in self.node:
            for dest in self.edge[src]:
                result = result + src.get_name() + '->' + dest.get_name() + '\n'
        return result[:-1]


