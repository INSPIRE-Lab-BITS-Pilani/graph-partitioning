#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  crossover.py

import random

#P - n elements, Q - 2n elements
def ODPX(P, k, n):
    Q = []
    for i in range(0, n/2):
        r1 = random.randrange(0, n/2)
        r2 = random.randrange(0, n/2)
        q1, q2, q3, q4 = ODPX(P[r1], P[r2], k, n)
        Q.append(q1)
        Q.append(q2)
        Q.append(q3)
        Q.append(q4)
    return Q
