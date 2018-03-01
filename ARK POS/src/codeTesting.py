# # import sys
# # from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
# # from PyQt5.QtGui import QIcon
# # from PyQt5.QtCore import pyqtSlot
# #
# # class App(QDialog):
# #
# #     def __init__(self):
# #         super().__init__()
# #         self.title = 'PyQt5 layout - pythonspot.com'
# #         self.left = 10
# #         self.top = 10
# #         self.width = 320
# #         self.height = 100
# #         self.initUI()
# #
# #     def initUI(self):
# #         self.setWindowTitle(self.title)
# #         self.setGeometry(self.left, self.top, self.width, self.height)
# #
# #         self.createGridLayout()
# #
# #         windowLayout = QVBoxLayout()
# #         windowLayout.addWidget(self.horizontalGroupBox)
# #         self.setLayout(windowLayout)
# #
# #         self.show()
# #
# #     def createGridLayout(self):
# #         self.horizontalGroupBox = QGroupBox("Grid")
# #         layout = QGridLayout()
# #         layout.setColumnStretch(1, 4)
# #         layout.setColumnStretch(2, 4)
# #
# #         layout.addWidget(QPushButton('1'),0,0)
# #         layout.addWidget(QPushButton('2'),0,1)
# #         layout.addWidget(QPushButton('3'),0,2)
# #         layout.addWidget(QPushButton('4'),1,0)
# #         layout.addWidget(QPushButton('5'),1,1)
# #         layout.addWidget(QPushButton('6'),1,2)
# #         layout.addWidget(QPushButton('7'),2,0)
# #         layout.addWidget(QPushButton('8'),2,1)
# #         layout.addWidget(QPushButton('9'),2,2)
# #
# #         self.horizontalGroupBox.setLayout(layout)
# #
# #
# #
# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     ex = App()
# #     sys.exit(app.exec_())
#
# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot
#
# class App(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 tabs - pythonspot.com'
#         self.left = 0
#         self.top = 0
#         self.width = 300
#         self.height = 200
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         self.table_widget = MyTableWidget(self)
#         self.setCentralWidget(self.table_widget)
#
#         self.show()
#
# class MyTableWidget(QWidget):
#
#     def __init__(self, parent):
#         super(QWidget, self).__init__(parent)
#         self.layout = QVBoxLayout(self)
#
#         # Initialize tab screen
#         self.tabs = QTabWidget()
#         self.tab1 = QWidget()
#         self.tab2 = QWidget()
#         self.tabs.resize(300,200)
#
#         # Add tabs
#         self.tabs.addTab(self.tab1,"Tab 1")
#         self.tabs.addTab(self.tab2,"Tab 2")
#
#         # Create first tab
#         self.tab1.layout = QVBoxLayout(self)
#         self.pushButton1 = QPushButton("PyQt5 button")
#         self.tab1.layout.addWidget(self.pushButton1)
#         self.tab1.setLayout(self.tab1.layout)
#
#         # Add tabs to widget
#         self.layout.addWidget(self.tabs)
#         self.setLayout(self.layout)
#
#     @pyqtSlot()
#     def on_click(self):
#         print("\n")
#         for currentQTableWidgetItem in self.tableWidget.selectedItems():
#             print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())
#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        label1 = QLabel("Example content contained in a tab.")
        label2 = QLabel("More example text in the second tab.")

        tabwidget = QTabWidget()
        tabwidget.addTab(label1, "Tab 1")
        tabwidget.addTab(label2, "Tab 2")
        layout.addWidget(tabwidget, 0, 0)

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
