# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InputWindow(object):
    def setupUi(self, InputWindow):
        InputWindow.setObjectName("InputWindow")
        InputWindow.resize(1000, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InputWindow.sizePolicy().hasHeightForWidth())
        InputWindow.setSizePolicy(sizePolicy)
        InputWindow.setMinimumSize(QtCore.QSize(100, 600))
        InputWindow.setMaximumSize(QtCore.QSize(1000, 600))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        InputWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(InputWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 151, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 171, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.old_holes_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.old_holes_tableWidget.setGeometry(QtCore.QRect(10, 150, 361, 251))
        self.old_holes_tableWidget.setObjectName("old_holes_tableWidget")
        self.old_holes_tableWidget.setColumnCount(2)
        self.old_holes_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.old_holes_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.old_holes_tableWidget.setHorizontalHeaderItem(1, item)
        self.old_holes_tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.add_hole_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_hole_pushButton.setGeometry(QtCore.QRect(430, 180, 201, 41))
        self.add_hole_pushButton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.add_hole_pushButton.setObjectName("add_hole_pushButton")
        self.delete_hole_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.delete_hole_pushButton.setGeometry(QtCore.QRect(430, 250, 201, 41))
        self.delete_hole_pushButton.setStyleSheet("background-color: rgb(179, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.delete_hole_pushButton.setObjectName("delete_hole_pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 40, 91, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.size_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.size_doubleSpinBox.setGeometry(QtCore.QRect(180, 40, 141, 22))
        self.size_doubleSpinBox.setDecimals(8)
        self.size_doubleSpinBox.setMaximum(1e+78)
        self.size_doubleSpinBox.setObjectName("size_doubleSpinBox")
        self.add_old_processes_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_old_processes_pushButton.setGeometry(QtCore.QRect(560, 400, 141, 51))
        self.add_old_processes_pushButton.setObjectName("add_old_processes_pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 390, 611, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        InputWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(InputWindow)
        self.statusbar.setObjectName("statusbar")
        InputWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(InputWindow)
        self.toolBar.setObjectName("toolBar")
        InputWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar = QtWidgets.QMenuBar(InputWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        InputWindow.setMenuBar(self.menubar)
        self.actionopen = QtWidgets.QAction(InputWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction(InputWindow)
        self.actionsave.setObjectName("actionsave")
        self.actioncopy = QtWidgets.QAction(InputWindow)
        self.actioncopy.setObjectName("actioncopy")
        self.actionpaste = QtWidgets.QAction(InputWindow)
        self.actionpaste.setObjectName("actionpaste")

        self.retranslateUi(InputWindow)
        QtCore.QMetaObject.connectSlotsByName(InputWindow)

    def retranslateUi(self, InputWindow):
        _translate = QtCore.QCoreApplication.translate
        InputWindow.setWindowTitle(_translate("InputWindow", "Inputs"))
        self.label.setText(_translate("InputWindow", "Enter the Memory size"))
        self.label_2.setText(_translate("InputWindow", "Enter the old holes:"))
        item = self.old_holes_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("InputWindow", "Start address"))
        item = self.old_holes_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("InputWindow", "Size"))
        self.add_hole_pushButton.setText(_translate("InputWindow", "Add a row for a hole"))
        self.delete_hole_pushButton.setText(_translate("InputWindow", "Delete the last row"))
        self.label_3.setText(_translate("InputWindow", "In KB"))
        self.add_old_processes_pushButton.setText(_translate("InputWindow", "Add Processes"))
        self.label_4.setText(_translate("InputWindow", "To begin adding allocating new processes, Press  this button:"))
        self.toolBar.setWindowTitle(_translate("InputWindow", "toolBar"))
        self.actionopen.setText(_translate("InputWindow", "open"))
        self.actionsave.setText(_translate("InputWindow", "save"))
        self.actioncopy.setText(_translate("InputWindow", "copy"))
        self.actionpaste.setText(_translate("InputWindow", "paste"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InputWindow = QtWidgets.QMainWindow()
    ui = Ui_InputWindow()
    ui.setupUi(InputWindow)
    InputWindow.show()
    sys.exit(app.exec_())
