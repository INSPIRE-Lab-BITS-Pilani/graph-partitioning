#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  driver.py

import random

from compute_fitness import compute_fitness
from crossover import crossover
from create_partitions import create_partitions, weight_part

def driver(G, W, k, MAX_GEN):
    n = len(G)
    P = []
    for i in range(2*n):
        temp = range(n)
        random.shuffle(temp)
        P.append(tuple(temp))
    for i in range(MAX_GEN):
        fitness = compute_fitness(G, W, k, P)
        fitness.sort(key=lambda tup: tup[1])
        P = [fitness[j][0] for j in range(n)]
        P = crossover(P, k, n)
    fitness = compute_fitness(G, W, k, P)
    fitness.sort(key=lambda tup: tup[1])
    p = fitness[0][0]
    return create_partitions(G, W, k, p)

def main(args):
    if len(args) != 3:
        print "Usage: python2 driver.py <graphFile> <vertexWeightsFile>"
        return -1
    f = open(args[1], 'r')
    G = [ map(int,line.split(' ')) for line in f ]
    f1 = open('VertexWeights.txt', 'r')
    W = [int(line) for line in f1]
    k = 2
    partitions = driver(G, W, k, 500)
    print partitions
    print weight_part(partitions[0], W)
    print weight_part(partitions[1], W)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
