#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  crossover.py

import random

from ODPX import ODPX

#P - n elements, Q - 2n elements
def crossover(P, k, n):
    Q = []
    for i in range(0, n/2):
        r1 = random.randrange(0, n)
        r2 = random.randrange(0, n)
        q1, q2, q3, q4 = ODPX(list(P[r1]), list(P[r2]), k, n)
        Q.append(tuple(q1))
        Q.append(tuple(q2))
        Q.append(tuple(q3))
        Q.append(tuple(q4))
    return Q
