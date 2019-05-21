#!/usr/bin/python3
# -*-conding:utf-8 -*-

__author__ = 'Zhang Han'

'动态规划'

def build_opt_btree(wp, wq):
    num = len(wp) + 1
    assert len(wq) == num, "value error"
    w = [[0]*num for i in range(num)]
    c  = [[0]*num for i in range(num)]
    r  = [[0]*num for i in range(num)]

    for i in range(num):
        w[i][i] = wq[i]
        for j in range(i+1, num):
            w[i][j] = w[i][j-1] + wp[j-1] + wq[j]

    for i in range(num-1):
            r[i][i+1] = i
            c[i][i+1] = w[i][i+1]

    for m in range(2, num):
        '''包含m个节点的n-m+1课树'''
        for i in range(0, num-m):
            k0, j = i, i + m
            wmin = float('inf')
            for k in range(i, j):
                if c[i][k] + c[k+1][j] < wmin:
                    wmin = c[i][k] + c[k+1][j]
                    k0 = k
            r[i][j] = k0
            c[i][j] = w[i][j] + wmin
    return c, r

a, b = build_opt_btree([2,3,7], [2,1,4,9])
print(a)
print(b)

