#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  create_partitions.py

def create_partitions(G, W, k, p):
    partitions = []
    free = []
    n = len(p)
    for i in range(k):
        partitions.append([p[i]])
        free.append(False)
    for i in range(k, n):
        free.append(True)
    someFree = True
    while someFree:
        someFree = False
        for i in range(k, n):
            if free[i]:
                smallest = float('inf')
                index = -1
                for l in range(k):
                    for j in range(n):
                        if G[p[i]][j] > 0 and j in partitions[l]:
                            if weight_part(partitions[l], W) < smallest:
                                smallest = weight_part(partitions[l], W)
                                index = l
                if index == -1:
                    someFree = True
                else:
                    partitions[index].append(p[i])
                    free[i] = False
    return partitions

def weight_part(part, W):
    w = 0
    for i in part:
        w += W[i]
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
    p = (6,5,2,9,4,0,10,8,3,11,7,1)
    #print create_partitions(G, k, p)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
