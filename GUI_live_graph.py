#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QMessageBox, QDesktopWidget, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import QPropertyAnimation

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import itertools

import numpy as np

import time
live_graph = 0
fig = 0


class Window(QWidget):
    def __init__(self):
        super().__init__()

        title = "Weather and time"
        top = 100
        left = 100
        width = 800
        height = 400

        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon('train.jpg'))
        self.setWindowTitle(title)
        self.initUI()

    def initUI(self):
        global live_graph
        live_graph = LiveGraph(self, width=8, height=4)
        live_graph.move(0, 0)

        live_graph.animate()

        self.button(x=500, y=350)
        self.exit_button(x=700, y=350)
        self.center()

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def button(self, x, y, label: str = "button"):
        # self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton(label, self)
        btn.setToolTip('This button does: <b>Nothing</b> :D')
        btn.clicked.connect(self.action_button_1)
        btn.resize(btn.sizeHint())
        btn.move(x, y)

    def exit_button(self, x, y):
        qbtn = QPushButton('Quit', self)
        qbtn.setToolTip('This button: <b>exit</b> the program')
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(x, y)

    def action_button_1(self):
        buttonReply = QMessageBox.question(
            self, 'Pop up Message', "Do you like the program?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        print(int(buttonReply))
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
            # live_graph.animate()
        if buttonReply == QMessageBox.No:
            print('No clicked.')
        if buttonReply == QMessageBox.Cancel:
            print('Cancel')


class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.plot()

    def plot(self):
        x = np.array([50, 30, 40])
        labels = ["One", "Two", "Three"]
        ax = self.figure.add_subplot(111)
        ax.pie(x, labels=labels)


class LiveGraph(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        global fig
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        #fig = plt.figure(1, (10, 10))
        #ax1 = fig.add_subplot(1, 1, 1)
        ani = animation.FuncAnimation(fig, self.animate(), interval=10000)
        # self.animate()
        plt.show()
        # self.animate()

    def animate(self):
        print("animating")
        graph_data = open('cpu_temp.csv', 'r').read()
        lines = graph_data.split('\n')
        xs = []
        ys: float = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(x)
                ys.append(float(y))
        # self.scatter(xs, ys)
        self.plotGraph(xs, ys)
        plt.show()

    def plotGraph(self, xs, ys: float):
        #labels = ["One", "Two", "Three"]
        ax = self.figure.add_subplot(111)
        ax.clear()
        #ax.scatter(xs, ys)
        ax.plot(xs, ys)


if __name__ == '__main__':
    my_app = QApplication(sys.argv)
    window = Window()
    # plt.show()
    print("Main")
    # live_graph.animate()
    # window.setToolTip('test')
    #ani = animation.FuncAnimation(fig, live_graph.animate(), interval=10000)
    # plt.show()
    sys.exit(my_app.exec_())


# QToolTip.setFont(QFont('SansSerif', 10))
