#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This program is a restaurant menu containing tabs for category of types of dishes served at the restaurant.

"""

"""
Things to work on.
-Added tabs but button is overlaying it.  Fix it so that button is on each tab.
-Button is no longer working.  
"""

import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class POS_App(QWidget):

    def __init__(self):
        super().__init__()
        self.left = 600
        self.top = 350
        self.width = 620
        self.height = 400
        self.initUI()


    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height) # Creates size of boarder windows for the application
        self.setWindowTitle('ARK Menu')    #Title for the program window
        layout = QGridLayout()
        self.setLayout(layout)
        tabWidget = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        tabWidget.addTab(self.tab1,"tab 1")
        tabWidget.addTab(self.tab2,"tab 2")
        layout.addWidget(tabWidget, 0, 0)
#         implementing buttons
        button = QPushButton('PyQt5 button', self)
        # self.tab1.layout.addWidget(self.button)
        button.move(200,140) #size of button
        button.clicked.connect(self.on_click) #this is an event response when clicking the buttons.


        # button2  = QPushButton('Finish', self)
        # button2.move(100, 140)
        # button2.clicked.connect(self.on_click)
        #
        # button3 = QPushButton('Print', self)
        # button3.move(300, 140)
        # button3.clicked.connect(self.on_click2)
        #
        # button4 = QPushButton('New Order', self)
        # button4.move(400, 140)
        # button4.clicked.connect(self.on_click3)

        self.show()
        # print("working")



    # @pyqtSlot
    # def tabClick(self):


    def on_click(self):
        filename = "pythonOrder.txt"
        myfile = open(filename, 'a') # opens a text file to use for keeping the orders
        sender = self.sender()# receives event action from the buttons
        self.statusBar().showMessage(sender.text() + ' was pressed') # used to show which button was pressed
        myfile.write(sender.text() + ' ')# adds the pressed item button to the text file


# this method is used to print to the assign default printer.
    def on_click2(self):
        os.startfile("C:/Users/Alex Lee/Documents/Github/Python/src/MainActivity/pythonOrder.txt", "print")

# this method is called to delete and create a new text file for the next order.
    def on_click3(self):
        filename = "pythonOrder.txt"
        myfile = open(filename, 'w')



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = POS_App()
    sys.exit(app.exec_())
