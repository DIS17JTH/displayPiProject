#! /usr/bin/python3

from time import sleep, strftime, time
import matplotlib.pyplot as plt
import numpy as np

plt.ion()
x = [i for i in range(20, 100, 3)]
y = [i for i in range(len(x))]

# draw a graph with data


def graph():
    # plt.clf()
    #plt.scatter(x, y)
    plt.plot(x, y)
    # plt.draw()


while True:
    graph()
    plt.show()
    sleep(1)
