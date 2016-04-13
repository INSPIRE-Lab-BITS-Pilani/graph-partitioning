#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  compute_fitness.py

from create_partitions import create_partitions

def compute_fitness(G, k, P):
    fitness = []
    for p in P:
        parts = create_partitions(G, k, p)
        wp = [weight_part(part, G) for part in parts]
        fitness.append((p, max(wp) - min(wp)))
    return fitness

def weight_part(part, G):
    w = 0
    for i in part:
        for j in part:
            if G[i][j] > 0:
                w += G[i][j]
    return w

def main(args):
    G = [[0 for j in range(12)] for i in range(12)]
    X = [[1,2,3],[0,7,8],[0,3,7],[0,2,4,5],[3,5],[3,4,7],[7,8,10],[1,2,5,6],[1,6,9],[8,11],[6,11],[9,10]]
    i = 0
    for l in X:
        for j in l:
            G[i][j] = 1
        i += 1
    k = 3
    P = [(6,5,2,9,4,0,10,8,3,11,7,1)]
    print compute_fitness(G, k, P)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
