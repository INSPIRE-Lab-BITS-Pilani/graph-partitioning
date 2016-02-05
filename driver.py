#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  driver.py

import random

from compute_fitness import compute_fitness
from crossover import crossover
from create_partitions import create_partitions

def driver(G, k, MAX_GEN):
    n = len(G)
    P = []
    for i in range(2*n):
        temp = range(n)
        random.shuffle(temp)
        P.append(tuple(temp))
    for i in range(MAX_GEN):
        fitness = compute_fitness(G, k, P)
        fitness.sort(key=lambda tup: tup[1])
        P = [fitness[j][0] for j in range(n)]
        P = crossover(P, k, n)
    fitness = compute_fitness(G, k, P)
    fitness.sort(key=lambda tup: tup[1])
    p = fitness[0][0]
    return create_partitions(G, k, p)

def main(args):
    G = [[0 for j in range(12)] for i in range(12)]
    X = [[1,2,3],[0,7,8],[0,3,7],[0,2,4,5],[3,5],[3,4,7],[7,8,10],[1,2,5,6],[1,6,9],[8,11],[6,11],[9,10]]
    i = 0
    for l in X:
        for j in l:
            G[i][j] = 1
        i += 1
    k = 3
    print driver(G, k, 500)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
