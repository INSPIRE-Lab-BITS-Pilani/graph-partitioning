#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  ODPX.py

import random

def ODPX(p1, p2, k, n):
    I = [val for val in p1[:k] if val in p2[:k]]
    for i in range(0, k):
        if not (p1[i] in I):
            j = random.randrange(k, n)
            temp = p1[i]
            p1[i] = p1[j]
            p1[j] = temp
    J = p1[:k]
    for i in range(0, k):
        if not (p2[i] in I):
            j = random.randrange(k, n)
            while p2[j] in J:
                j = random.randrange(k, n)
            temp = p2[i]
            p2[i] = p2[j]
            p2[j] = temp
    q1 = p1[:k]
    q2 = p2[:k]
    q3 = p1[:k]
    q4 = p2[:k]
    L1 = []
    L2 = []
    for i in range(0, 2*(n - k)):
        if (i%2 == 1) is True:
            L1.append(p2[k + (i - 1)/2])
            L2.append(p1[k + (i - 1)/2])
        else:
            L1.append(p1[k + i/2])
            L2.append(p2[k + i/2])
    for i in range(0, 2*(n - k)):
        if not (L1[i] in q1):
            q1.append(L1[i])
        else:
            q2.append(L1[i])
        if not (L2[i] in q4):
            q4.append(L2[i])
        else:
            q3.append(L2[i])
    return q1, q2, q3, q4

def main(args):
    k = 3
    n = 12
    q1, q2, q3, q4 = ODPX([5, 3, 7, 4, 11, 8, 2, 12, 1, 9, 6, 10], [7, 6, 3, 10, 5, 1, 11, 9, 4, 12, 8, 2], k, n)
    print q1
    print q2
    print q3
    print q4
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
