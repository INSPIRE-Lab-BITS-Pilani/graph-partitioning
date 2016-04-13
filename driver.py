#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  driver.py

import random

from compute_fitness import compute_fitness, weight_part
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
    #f = open('ConnectivityGraph.txt', 'r')
    #G = [ map(int,line.split(' ')) for line in f ]
    #k = 10
    G = [[0, 2, 0, 5, 0, 0], [2, 0, 3, 0, 1, 0], [0, 3, 0, 4, 0, 0], [5, 0, 4, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0]]
    k = 2
    partitions = driver(G, k, 500)
    print partitions
    print weight_part(partitions[0], G)
    print weight_part(partitions[1], G)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
