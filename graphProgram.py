#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from time import sleep, strftime, time
# import matplotlib as mplib
# matplotlib.use('PS')
# mplib.use('WXAgg')

x = [i for i in range(20, 100, 3)]
y = [i for i in range(len(x))]

plt.ion()
plt.title("interactive test")
plt.xlabel("index")


def graph():  # draw a graph with data
    plt.clf()
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.draw()


while True:
    graph()
    plt.show()
    sleep(1)
