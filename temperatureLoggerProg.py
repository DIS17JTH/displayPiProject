#! /usr/bin/python3

from gpiozero import CPUTemperature
from time import sleep, strftime, time
import matplotlib.pyplot as plt

cpu = CPUTemperature()

plt.ion()
x = []
y = []

#write temp to file
def writeTemp(temp):
    with open("/home/pi/cpu_temp.csv", "a") as log:
        log.write("{},{}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

#draw a graph of the data
def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.draw()


while True:
    temp = cpu.temperature
    writeTemp(temp)
    graph(temp)
    sleep(1)
