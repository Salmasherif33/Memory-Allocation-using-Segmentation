# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'First_Try.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Plotting import Ui_ChartWindow

myList = [
            {
                'name': "P1:code",
                'start': 0,
                'end': 70
            },
            {
                'name': "hole1",
                'start': 70,
                'end': 150
            },
            {
                'name': "P2:Data",
                'start': 150,
                'end': 300
            },
            {
                'name': "P2:code",
                'start': 300,
                'end': 600
            },
            {
                'name': "P2:Data",
                'start': 600,
                'end': 685
            },
            {
                'name': "P2:Data",
                'start': 600,
                'end': 685
            },
            {
                'name': "P2:Data",
                'start': 600,
                'end': 685
            },
            {
                'name': "P2:code",
                'start': 300,
                'end': 600
            },
            {
                'name': "P2:Data",
                'start': 600,
                'end': 685
            },
            {
                'name': "P2:Data",
                'start': 600,
                'end': 685
            },
            {
                'name': "P2:Data",
                'start': 900,
                'end': 1250
            }
        ]
class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ChartWindow()
        self.ui.setupUi(self.window,myList)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 714)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 340, 171, 71))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.openWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Draw"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
