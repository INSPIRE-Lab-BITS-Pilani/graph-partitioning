#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  driver.py

import random

from compute_fitness import compute_fitness
from crossover import crossover
from create_partitions import create_partitions
from Tkinter import Tk, Label, Entry, Button, END, mainloop
from tkFileDialog import askopenfilename
from tkMessageBox import showerror, showinfo

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

def fileChoose():
    filename = askopenfilename()
    if filename:
        b1.config(text = filename)

def fileChoose1():
    filename1 = askopenfilename()
    if filename1:
        b2.config(text = filename1)

def doIt():
    if b1["text"] == "Choose":
        showerror("No File", "Please choose a valid graph file first!")
        return
    elif b2["text"] == "Choose":
        showerror("No File", "Please choose a valid vertex weights file first!")
        return
    G = [ map(int,line.split(' ')) for line in open(b1["text"], 'r') ]
    W = [int(line) for line in open(b2["text"], 'r')]
    k = int(e1.get())
    MAX_GEN = int(e2.get())
    partitions = driver(G, W, k, MAX_GEN)
    outfile = open(b1["text"][0 : b1["text"].find('.')] + "_" + str(k) + "_"
                    + str(MAX_GEN) + "_out.txt", 'w')
    outfile.write(str(partitions) + '\n')
    showinfo("Obtained Partition", "Answer has been written to " + outfile.name)

master = Tk()
master.title("Graph Partitioning")
Label(master, text = "Graph file").grid(row = 0)
Label(master, text = "Vertex weights file").grid(row = 1)
Label(master, text = "Number of subgraphs").grid(row = 2)
Label(master, text = "Max generations").grid(row = 3)

b1 = Button(text = "Choose", command = fileChoose)
b2 = Button(text = "Choose", command = fileChoose1)
e1 = Entry(master)
e1.insert(END, 2)
e2 = Entry(master)
e2.insert(END, 500)
b3 = Button(text = "Compute", command = doIt).grid(row = 4, column = 0)
b4 = Button(text = "Quit", command = master.quit).grid(row = 4, column = 1)

b1.grid(row = 0, column = 1)
b2.grid(row = 1, column = 1)
e1.grid(row = 2, column = 1)
e2.grid(row = 3, column = 1)

mainloop()
