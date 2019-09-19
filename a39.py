#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.deziValue = ""
        self.hexValue = ""

    def initUi(self):
        self.resize(300, 200)
        self.setWindowTitle("Aufgabe 39")

        # Populate UI
        deziLabel = QLabel("Dezimalzahl", self)
        deziText = QLineEdit(self)
        deziText.textChanged[str].connect(self.onDeziTextChange)
        hexLabel = QLabel("Hexazahl", self)
        self.hexText = QLineEdit(self)
        calcButton = QPushButton("Berechnen", self)
        calcButton.clicked.connect(self.onCalc)

        grid = QGridLayout()
        grid.addWidget(deziLabel, 0, 0)
        grid.addWidget(deziText,  0, 1)
        grid.addWidget(hexLabel, 1, 0)
        grid.addWidget(self.hexText,  1, 1)
        grid.addWidget(calcButton, 2, 0, 1, 2)

        self.setLayout(grid)
        self.show()

    def onDeziTextChange(self, newString):
        self.deziValue = newString

    def onCalc(self):
        try:
            hexVal = int(self.deziValue)
            newText = f"0x{hexVal:x}"
        except:
            newText = "Please input a number!"
        self.hexText.setText(newText)

app = QApplication(sys.argv)
w=MyWidget()
app.exec_()
