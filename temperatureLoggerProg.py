#! /usr/bin/python3

from gpiozero import CPUTemperature
from time import sleep, strftime, time
import matplotlib.pyplot as plt

cpu = CPUTemperature()

# plt.ion() -> BUG
x = []
y = []


def writeTemp(temp):  # write temp to file
    with open("/home/pi/projectScreen/cpu_temp.csv", "a") as log:
        log.write("{},{}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(temp)))


def graph(temp):  # draw a graph of the data ->not working
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.draw()


while True:
    temp = cpu.temperature
    writeTemp(temp)
    # graph(temp)
    sleep(1)
