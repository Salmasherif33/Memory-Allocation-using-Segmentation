# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

before_first_num1 = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n""p, li { white-space: pre-wrap; }\n""</style></head><body"
new_process = " bgcolor=\"#00acff\" "
hole = " bgcolor=\"#FA669A\" "
old_process = " bgcolor=\"#e3f55a\" "
color = " bgcolor=\"#e3f55a\" "
before_first_num2 = " style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">"
before_name = "</span></p>\n""<p style=\" margin-top:13px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">              "
far_before_last_num = "</span></p>\n""<p style=\" margin-top:"
before_last_num= "px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">"
ending = "</span></p></body></html>"


class Ui_Window_test(object):
    def setupUi(self, Window_test):
        Window_test.setObjectName("Window_test")
        #Window_test.resize(1500, 954)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Window_test.sizePolicy().hasHeightForWidth())
        Window_test.setSizePolicy(sizePolicy)
        Window_test.setMinimumSize(QtCore.QSize(1500, 1000))
        Window_test.setMaximumSize(QtCore.QSize(1500, 1000))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        Window_test.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Window_test)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 200, 51))
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
        self.label_2.setGeometry(QtCore.QRect(10, 70, 171, 41))
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
        self.old_holes_tableWidget.setGeometry(QtCore.QRect(10, 130, 381, 331))
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
        self.add_hole_pushButton.setGeometry(QtCore.QRect(210, 470, 181, 41))
        self.add_hole_pushButton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.add_hole_pushButton.setObjectName("add_hole_pushButton")
        self.delete_hole_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.delete_hole_pushButton.setGeometry(QtCore.QRect(10, 470, 181, 41))
        self.delete_hole_pushButton.setStyleSheet("background-color: rgb(179, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.delete_hole_pushButton.setObjectName("delete_hole_pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 30, 61, 21))
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
        self.size_doubleSpinBox.setGeometry(QtCore.QRect(220, 20, 141, 31))
        self.size_doubleSpinBox.setDecimals(8)
        self.size_doubleSpinBox.setMaximum(1e+78)
        self.size_doubleSpinBox.setObjectName("size_doubleSpinBox")
        self.process_table = QtWidgets.QTableWidget(self.centralwidget)
        self.process_table.setGeometry(QtCore.QRect(440, 140, 411, 331))
        self.process_table.setShowGrid(True)
        self.process_table.setRowCount(0)
        self.process_table.setObjectName("process_table")
        self.process_table.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.process_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.process_table.setHorizontalHeaderItem(1, item)
        self.process_table.horizontalHeader().setDefaultSectionSize(200)
        self.process_table.horizontalHeader().setHighlightSections(True)
        self.add_segment_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_segment_button.setGeometry(QtCore.QRect(470, 480, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_segment_button.setFont(font)
        self.add_segment_button.setObjectName("add_segment_button")
        self.allocate_button = QtWidgets.QPushButton(self.centralwidget)
        self.allocate_button.setGeometry(QtCore.QRect(650, 480, 200, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.allocate_button.setFont(font)
        self.allocate_button.setStyleSheet("\n"
"background-color: rgb(6, 239, 33);\n"
"")
        self.allocate_button.setObjectName("allocate_button")
        self.add_process_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_process_button.setGeometry(QtCore.QRect(900, 160, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.add_process_button.setFont(font)
        self.add_process_button.setStyleSheet("")
        self.add_process_button.setObjectName("add_process_button")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 90, 400, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 10, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 10, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1150, 10, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.number_of_segments = QtWidgets.QSpinBox(self.centralwidget)
        self.number_of_segments.setGeometry(QtCore.QRect(760, 100, 71, 31))
        self.number_of_segments.setObjectName("number_of_segments")
        self.algorithm = QtWidgets.QComboBox(self.centralwidget)
        self.algorithm.setGeometry(QtCore.QRect(760, 20, 101, 31))
        self.algorithm.setObjectName("algorithm")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.algorithm.addItem("")
        self.deallocate_button = QtWidgets.QPushButton(self.centralwidget)
        self.deallocate_button.setGeometry(QtCore.QRect(900, 240, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.deallocate_button.setFont(font)
        self.deallocate_button.setStyleSheet("")
        self.deallocate_button.setObjectName("deallocate_button")
        self.memory_button = QtWidgets.QPushButton(self.centralwidget)
        self.memory_button.setGeometry(QtCore.QRect(900, 320, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.memory_button.setFont(font)
        self.memory_button.setStyleSheet("")
        self.memory_button.setObjectName("memory_button")
        self.add_old_processes_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_old_processes_pushButton.setGeometry(QtCore.QRect(150, 530, 141, 51))
        self.add_old_processes_pushButton.setObjectName("add_old_processes_pushButton")
        Window_test.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Window_test)
        self.statusbar.setObjectName("statusbar")
        Window_test.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(Window_test)
        self.toolBar.setObjectName("toolBar")
        Window_test.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar = QtWidgets.QMenuBar(Window_test)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 26))
        self.menubar.setObjectName("menubar")
        Window_test.setMenuBar(self.menubar)
        self.actionopen = QtWidgets.QAction(Window_test)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction(Window_test)
        self.actionsave.setObjectName("actionsave")
        self.actioncopy = QtWidgets.QAction(Window_test)
        self.actioncopy.setObjectName("actioncopy")
        self.actionpaste = QtWidgets.QAction(Window_test)
        self.actionpaste.setObjectName("actionpaste")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(1075, 50, 221, 500))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 198, 50))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        ########################################
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(870, 400, 171, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser_100 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_100.setObjectName("textBrowser_100")
        self.gridLayout.addWidget(self.textBrowser_100, 0, 1, 1, 1)
        self.label_100 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_100.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_100.setObjectName("label_100")
        self.gridLayout.addWidget(self.label_100, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_111 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_111.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_111.setObjectName("label_111")
        self.gridLayout.addWidget(self.label_111, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.textBrowser_111 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_111.setObjectName("textBrowser_111")
        self.gridLayout.addWidget(self.textBrowser_111, 1, 1, 1, 1)
        self.textBrowser_122 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_122.setObjectName("textBrowser_122")
        self.gridLayout.addWidget(self.textBrowser_122, 2, 1, 1, 1)
        self.label_122 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_122.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_122.setObjectName("label_122")
        self.gridLayout.addWidget(self.label_122, 2, 0, 1, 1)
        Window_test.setCentralWidget(self.centralwidget)
        
        ########################################

        
        # start = 0
        # for i in range(0,len(myList)):
        #     text = str(i)
        #     self.text = QtWidgets.QTextBrowser(self.centralwidget)
        #     length = myList[i]['end'] - myList[i]['start']
        #     self.text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        #     self.text.setObjectName(text)
        #     self.verticalLayout_2.addWidget(self.text)
        #     start += length
        #     Window_test.setCentralWidget(self.centralwidget)
        #     if myList[i]['name'][0] == 'P' or myList[i]['name'][0] == 'P' :
        #         color = new_process
        #     elif myList[i]['name'][0] == 'H' or myList[i]['name'][0] == 'h' :
        #         color = hole
        #     else:
        #         color = old_process
        #     self.retranslateUiDraw(Window_test,text,i,length,myList,color)
        #     QtCore.QTimer.singleShot(0, self.scrollAreaWidgetContents_2.adjustSize)
        #
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        Window_test.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window_test)
        QtCore.QMetaObject.connectSlotsByName(Window_test)

    def retranslateUi(self, Window_test):
        _translate = QtCore.QCoreApplication.translate
        Window_test.setWindowTitle(_translate("Window_test", "Inputs"))
        self.label.setText(_translate("Window_test", "Enter the Memory size"))
        self.label_2.setText(_translate("Window_test", "Enter the old holes:"))
        item = self.old_holes_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Window_test", "Start address"))
        item = self.old_holes_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Window_test", "Size"))
        self.add_hole_pushButton.setText(_translate("Window_test", "Add a row for a hole"))
        self.delete_hole_pushButton.setText(_translate("Window_test", "Delete the last row"))
        self.label_3.setText(_translate("Window_test", "In KB"))
        item = self.process_table.horizontalHeaderItem(0)
        item.setText(_translate("Window_test", "Segment name"))
        item = self.process_table.horizontalHeaderItem(1)
        item.setText(_translate("Window_test", "Segment Size"))
        self.add_segment_button.setText(_translate("Window_test", "Add Segment"))
        self.allocate_button.setText(_translate("Window_test", "Allocate this process"))
        self.add_process_button.setText(_translate("Window_test", "Add new process"))
        self.label_5.setText(_translate("Window_test", "number of segments of this process:"))
        self.label_6.setText(_translate("Window_test", "Algorithm of allocation:"))
        self.label_7.setText(_translate("Window_test", "Memory:"))
        self.algorithm.setItemText(0, _translate("Window_test", "First Fit"))
        self.algorithm.setItemText(1, _translate("Window_test", "Best Fit"))
        self.algorithm.setItemText(2, _translate("Window_test", "Worst Fit"))
        self.deallocate_button.setText(_translate("Window_test", "Deallocate"))
        self.memory_button.setText(_translate("Window_test", "Show Memory"))
        self.add_old_processes_pushButton.setText(_translate("Window_test", "submit holes"))
        self.toolBar.setWindowTitle(_translate("Window_test", "toolBar"))
        self.actionopen.setText(_translate("Window_test", "open"))
        self.actionsave.setText(_translate("Window_test", "save"))
        self.actioncopy.setText(_translate("Window_test", "copy"))
        self.actionpaste.setText(_translate("Window_test", "paste"))

        #Guide table part
        self.textBrowser_100.setHtml(_translate("Window_test", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#00acff\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_100.setText(_translate("Window_test", "New Pro"))
        self.label_111.setText(_translate("Window_test", "Hole"))
        self.textBrowser_111.setHtml(_translate("", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#fa669a\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_122.setHtml(_translate("Window_test", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#e3f55a\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_122.setText(_translate("Window_test", "Old Pro"))


    # def retranslateUiDraw(self, ChartWindow, text, i, length, myList, color):
    #     _translate = QtCore.QCoreApplication.translate
    #     self.text.setHtml(_translate("ChartWindow", before_first_num1 + color + before_first_num2 + str(
    #         myList[i]['start']) + before_name + myList[i]['name'] + far_before_last_num + "15" + before_last_num + str(
    #         myList[i]['end']) + ending))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window_test = QtWidgets.QMainWindow()
    ui = Ui_Window_test()
    myList = [
        {
            'name':"hole",
            'start': 0,
            'end':25
        },
        {
            'name': "process",
            'start': 25,
            'end': 250
        }
    ]
    ui.setupUi(Window_test)
    Window_test.show()
    sys.exit(app.exec_())