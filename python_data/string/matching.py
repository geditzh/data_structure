#!/usr/bin/python3
# -*- coding: utf-8 -*-

'string matching'

__author__ = 'Zhang Han'

def native_matching(t, p):
    n, m = len(t), len(p)
    j, i = 0, 0
    while j < n and i < m:
        if t[j] == p[i]:
            j, i = j + 1, i + 1
        else:
            j, i = j - i + 1, 0
    if i == m:
        return j - i
    else:
        return -1

# def matching_KMP(t, p):
#     n, m = len(t), len(p)
#     j, i = 0, 0
#     while j < n and i < m:
#         if i == -1 or t[j] == p[i]:
#             j, i = j +1, i + 1
#         else:
#             i = pnext[i]
#         return j - i
#     else:
#         return -1

def gen_pnext(p):
    m, k, i =len(p), -1, 0
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[k] == p[i]:
            i, k = i + 1, k + 1
            pnext[i] = k
        else:
            k = pnext[k]
    return pnext

def gen_pnext1(p):
    m, k, i = len(p), -1, 0
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[k] == p[i]:
            i, k = i + 1,k + 1
            if p[k] == p[i]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext

def matching_KMP(t, p):
    pnext = gen_pnext1(p)
    n, m = len(t), len(p)
    j, i = 0, 0
    while j < n and i < m:
        if t[j] == p[i] or i == -1:
            j, i = j + 1,i + 1
        else:
            i = pnext[i]
    if i == m:
        return j - i
    else:
        return -1

a = '00000000011223434000001234567890'
b ='7890'
print(native_matching(a, b))
print(matching_KMP(a, b))
print(gen_pnext1(a))
