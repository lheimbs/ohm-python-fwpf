#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
from a37 import Shape, Rect, Line, Group

class MyWidget(QWidget):
    def __init__(self, group):
        super().__init__()
        self.initUi()
        self.deziValue = ""
        self.hexValue = ""
        self.g=group

    def initUi(self):
        self.resize(300, 200)
        self.setWindowTitle("Aufgabe 39")
        self.show()

    def paintEvent(self, ev):
        qp = QPainter()
        w, h = self.width(), self.height()
        qp.begin(self)
        qp.setBrush(Qt.black)
        qp.setPen(Qt.black)
        qp.drawRect(0, 0, w, h)

        qp.setBrush(Qt.transparent)
        qp.setPen(Qt.yellow)
        g.draw(qp)

        qp.end()



if __name__ == "__main__":
    g=Group() 
    g.addShape(Line(20,  50, 20, 100)) 
    g.addShape(Line(20, 100, 40, 110)) 
    g.addShape(Line(40, 110, 60, 100)) 
    g.addShape(Line(60, 100, 60,  50)) 
    g.addShape(Line(60,  50, 40,  40)) 
    g.addShape(Line(40,  40, 20,  50)) 
    g.addShape(Line(25,  85, 40,  95)) 
    g.addShape(Line(40,  95, 55,  85)) 
    g.addShape(Rect(45, 60, 5 ,5)) 
    g.addShape(Rect(30, 60, 5 ,5)) 

    app = QApplication(sys.argv)
    w=MyWidget(g)
    app.exec_()