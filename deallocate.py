# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deallocate.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_deallo(object):
    def setupUi(self, deallo):
        deallo.setObjectName("deallo")
        deallo.resize(914, 709)
        self.old_process_table = QtWidgets.QTableWidget(deallo)
        self.old_process_table.setGeometry(QtCore.QRect(10, 160, 411, 351))
        self.old_process_table.setObjectName("old_process_table")
        self.old_process_table.setColumnCount(3)
        self.old_process_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.old_process_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.old_process_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.old_process_table.setHorizontalHeaderItem(2, item)
        self.old_process_table.horizontalHeader().setDefaultSectionSize(120)
        self.label = QtWidgets.QLabel(deallo)
        self.label.setGeometry(QtCore.QRect(20, 120, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.new_process_table = QtWidgets.QTableWidget(deallo)
        self.new_process_table.setGeometry(QtCore.QRect(450, 160, 411, 351))
        self.new_process_table.setObjectName("new_process_table")
        self.new_process_table.setColumnCount(2)
        self.new_process_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.new_process_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.new_process_table.setHorizontalHeaderItem(1, item)
        self.new_process_table.horizontalHeader().setDefaultSectionSize(150)
        self.label_2 = QtWidgets.QLabel(deallo)
        self.label_2.setGeometry(QtCore.QRect(460, 120, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.deallocate_old_button = QtWidgets.QPushButton(deallo)
        self.deallocate_old_button.setGeometry(QtCore.QRect(110, 520, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deallocate_old_button.setFont(font)
        self.deallocate_old_button.setObjectName("deallocate_old_button")
        self.label_3 = QtWidgets.QLabel(deallo)
        self.label_3.setGeometry(QtCore.QRect(220, 0, 441, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.deallocate_new_button = QtWidgets.QPushButton(deallo)
        self.deallocate_new_button.setGeometry(QtCore.QRect(560, 520, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deallocate_new_button.setFont(font)
        self.deallocate_new_button.setObjectName("deallocate_new_button")
        self.back_button = QtWidgets.QPushButton(deallo)
        self.back_button.setGeometry(QtCore.QRect(10, 40, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")
        
        self.retranslateUi(deallo)
        QtCore.QMetaObject.connectSlotsByName(deallo)

    def retranslateUi(self, deallo):
        _translate = QtCore.QCoreApplication.translate
        deallo.setWindowTitle(_translate("deallo", "Form"))
        item = self.old_process_table.horizontalHeaderItem(0)
        item.setText(_translate("deallo", "name"))
        item = self.old_process_table.horizontalHeaderItem(1)
        item.setText(_translate("deallo", "starting add."))
        item = self.old_process_table.horizontalHeaderItem(2)
        item.setText(_translate("deallo", "Size"))
        self.label.setText(_translate("deallo", "Old processes information"))
        item = self.new_process_table.horizontalHeaderItem(0)
        item.setText(_translate("deallo", "name"))
        item = self.new_process_table.horizontalHeaderItem(1)
        item.setText(_translate("deallo", "no. of segments"))
        self.label_2.setText(_translate("deallo", "New processes information"))
        self.deallocate_old_button.setText(_translate("deallo", "Deallocate old process"))
        self.label_3.setText(_translate("deallo", "Select only one process to deallocate"))
        self.deallocate_new_button.setText(_translate("deallo", "Deallocate added process"))
        self.back_button.setText(_translate("deallo", "Back to allocate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deallo = QtWidgets.QWidget()
    ui = Ui_deallo()
    ui.setupUi(deallo)
    deallo.show()
    sys.exit(app.exec_())
