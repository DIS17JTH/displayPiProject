#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QMessageBox, QDesktopWidget, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()
        self.setWindowTitle("Weather and time")
        self.resize(400, 400)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowIcon(QIcon('train.jpg'))
        self.button(150, 100)
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def button(self, x, y):
        #self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('Button', self)
        btn.setToolTip('This button does: <b>Nothing</b> :D')
        btn.resize(btn.sizeHint())
        btn.move(x-50, y-50)

        qbtn = QPushButton('Quit', self)
        qbtn.setToolTip('This button: <b>exit</b> the program')
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(x, y)


if __name__ == '__main__':
    my_app = QApplication(sys.argv)
    window = Window()
    # window.setToolTip('test')
    sys.exit(my_app.exec_())


#QToolTip.setFont(QFont('SansSerif', 10))
