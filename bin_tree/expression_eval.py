#!/usr/bin/python3
# -*- coding:utf-8 -*-

__author__ = 'Zhang Han'

def make_sum(a, b):
    return ('+', a, b)

def make_diff(a, b):
    return ('-', a, b)

def make_prod(a, b):
    return ('*', a, b)

def make_div(a, b ):
    return ('/', a, b)

def is_basic_exp(e):
    return not isinstance(e, tuple)

def is_number(a):
    return (isinstance(a, int) or isinstance(a, float) or isinstance(a, complex))

def eval_exp(e):
    if is_basic_exp(e):
        return e
    op, a, b = e[0], eval_exp(e[1]), eval_exp(e[2])     #这里进行了迭代计算
    if op == '+':
        if is_number(a) and is_number(b):
            return a + b
        if is_number(a) and b == 0:
            return a
        if a == 0 and is_number(b):
            return b
        return make_sum(a, b)
    if op == '-':
        if is_number(a) and is_number(b):
            return a - b
        if is_number(a) and b == 0:
            return a
        if a == 0 and is_number(b):
            return -b
        return make_diff(a, b)
    if op == '*':
        if is_number(a) and is_number(b):
            return a * b
        if is_number(a) and b == 0:
            return 0
        if a == 0 and is_number(b):
            return 0
        return make_prod(a, b)
    if op == '/':
        if is_number(a) and is_number(b):
            return a / b
        if is_number(a) and b == 0:
            raise ValueError('/0')
        if a == 0 and is_number(b):
            return 0
        if is_number(a) and b == 1:
            return a
        return make_div(a, b)

e1 = make_prod(9, make_sum(2, 5))
print(e1)
print(eval_exp(e1))


