import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QApplication
from deallocate import Ui_deallo
from Basic_UI import Ui_Window_test

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

# get (new dummy) list of maps from backend
new_dummy = [
    {
        'name': 'p1',
        'no_of_segments': 4

    },
    {
        'name': 'p2',
        'no_of_segments': 5

    },
    {
        'name': 'p3',
        'no_of_segments': 5

    },
]

class TestMainWindow(qtw.QMainWindow, Ui_Window_test):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Window_test()
        self.ui.setupUi(self)

        self.ui.size_doubleSpinBox.setMaximum(float('+inf'))
        self.ui.size_doubleSpinBox.setDecimals(5)
        self.ui.size_doubleSpinBox.clear()
        self.holes = []
        self.process_index = 0
        self.algorithm = self.ui.algorithm
        self.ui.process_table.insertRow(self.ui.process_table.rowCount())

        # add segment to process_table
        self.ui.add_segment_button.clicked.connect(self._addRow)

        # add new process
        self.ui.add_process_button.clicked.connect(self._addNewProcess)

        # allocate button
        self.ui.allocate_button.clicked.connect(self._addNewProcess)

        # show mem
        # self.ui.memory_button.clicked.connect(self.openWindow)

        # deallocate
        self.ui.deallocate_button.clicked.connect(self._deallocate)

        # button to add a hole
        self.ui.add_hole_pushButton.clicked.connect(self.add_hole_row)

        # button to delete the last row
        self.ui.delete_hole_pushButton.clicked.connect(self.delete_hole_row)

        # take mem size value
        memory_size = self.ui.size_doubleSpinBox.value()

        # button to add old processes
        self.ui.add_old_processes_pushButton.clicked.connect(self.add_old_processes)

        #button to update memory
        self.ui.memory_button.clicked.connect(self.showMemory)

    # Sharnoby's Part
    def retranslateUiDraw(self, ChartWindow, text, i, length, myList, color):
        _translate = QtCore.QCoreApplication.translate
        self.ui.text.setHtml(_translate("ChartWindow", before_first_num1 + color + before_first_num2 + str(
            myList[i]['start']) + before_name + myList[i]['name'] + far_before_last_num + "15" + before_last_num + str(
            myList[i]['end']) + ending))

    def showMemory(self):
        if len(self.holes) == 0:
            qtw.QMessageBox.critical(self, 'fail', "please,Fill the holes first")
            return

        if self.index == 0:
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
                'name': "Hole",
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
            self.index = 1
        else:
            myList = [
                {
                    'name': "Hole",
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
        for i in reversed(range(self.ui.verticalLayout_2.count())):
            self.ui.verticalLayout_2.itemAt(i).widget().setParent(None)
        #self.ui.verticalLayout_2.removeWidget(self.ui.text)

        start = 0
        for i in range(0, len(myList)):
            text = str(i)
            self.ui.text = qtw.QTextBrowser(self.ui.centralwidget)
            length = myList[i]['end'] - myList[i]['start']
            self.ui.text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
            self.ui.text.setObjectName(text)
            self.ui.verticalLayout_2.addWidget(self.ui.text)
            start += length
            # qtw.setCentralWidget(self.ui.centralwidget)
            if myList[i]['name'][0] == 'P' or myList[i]['name'][0] == 'P':
                color = new_process
            elif myList[i]['name'][0] == 'H' or myList[i]['name'][0] == 'h':
                color = hole
            else:
                color = old_process
            self.retranslateUiDraw(self, text, i, length, myList, color)
            QtCore.QTimer.singleShot(0, self.ui.scrollAreaWidgetContents_2.adjustSize)

    # salma's part
    def add_hole_row(self):
        self.ui.old_holes_tableWidget.insertRow(self.ui.old_holes_tableWidget.rowCount())

    def delete_hole_row(self):
        if self.ui.old_holes_tableWidget.rowCount() > 0:
            self.ui.old_holes_tableWidget.removeRow(self.ui.old_holes_tableWidget.rowCount() - 1)
        else:
            qtw.QMessageBox.critical(self, 'fail', 'There is no hole to delete')

    def add_old_processes(self):
        try:
            rowCount = self.ui.old_holes_tableWidget.rowCount()
            memory_size = self.ui.size_doubleSpinBox.value()
            if(memory_size == 0):
                qtw.QMessageBox.critical(self, 'fail', 'You have to add memory size')
                return
            flag = 0
            for row in range(rowCount):
                start_adrr = self.ui.old_holes_tableWidget.item(row, 0).text()
                size = self.ui.old_holes_tableWidget.item(row, 1).text()
                
                if  start_adrr.isnumeric() == False or size.isnumeric() == False:
                    qtw.QMessageBox.critical(self, 'fail', f'You have to add an unsigned number value in row {row+1}')
                    self.holes = []
                    flag = 1 
                    return
                if int(size) <=0 or int(start_adrr) < 0:
                    qtw.QMessageBox.critical(self, 'fail', 'You have to add a number greater than 0')
                    self.holes = []
                    flag = 1 
                    return

                else:
                    hole = [int(start_adrr), float(size)]
                    self.holes.append(hole)
                # send to back
            if len(self.holes) == 0 and flag == 0:
                qtw.QMessageBox.critical(self, 'fail', 'You have to add holes to add processes')
            else:
                qtw.QMessageBox.information(self, 'success', 'Holes are added sucessfully')
                self.ui.add_old_processes_pushButton.setEnabled(False)
                print(self.holes)
                print(memory_size)
        except:
            qtw.QMessageBox.critical(self, 'fail', 'Something went wrong')

    # mostafa's part
    def _addRow(self):
        no_of_segments = self.ui.number_of_segments.text()
        row_count = self.ui.process_table.rowCount()
        print(no_of_segments)

        # check that we don't enter all seg yet
        if row_count < (int(no_of_segments)):
            self.ui.process_table.insertRow(self.ui.process_table.rowCount())

        # check if the user didn't enter num of segments
        elif int(no_of_segments) == 0:
            qtw.QMessageBox.critical(self, 'fail', "please, enter number of segments of this process")

        # check if the user enter add seg and all the allowed seg are added
        else:
            qtw.QMessageBox.critical(self, 'fail', "all segments have been added")

    def _addNewProcess(self):
        if self.ui.number_of_segments.text() == '':
            qtw.QMessageBox.critical(self, 'fail', "please, enter number of segments of this process")
        elif len(self.holes) <= 0:
            qtw.QMessageBox.critical(self, 'warning', "please, add holes first")
        elif int(self.ui.number_of_segments.text()) <= 0:
            qtw.QMessageBox.critical(self, 'fail', "please, enter number of segments of this process")
        elif self.ui.process_table.rowCount() < int(self.ui.number_of_segments.text()):
            qtw.QMessageBox.critical(self, 'warning', "please, add all segments of this process")
        else:
            self.ui.algorithm.setEnabled(False)  # disable comboBox
            p = self.createSegments()
            print(p)
            self.process_index += 1
            print(self.process_index)
            self.clearScreen()

    def clearScreen(self):
        no_of_segments = self.ui.number_of_segments.text()
        if self.ui.process_table.rowCount() < int(no_of_segments):
            qtw.QMessageBox.critical(self, 'warning', "please, add all segments of this process")
        else:
            self.ui.number_of_segments.clear()
            while self.ui.process_table.rowCount() > 0:
                self.ui.process_table.removeRow(self.ui.process_table.rowCount() - 1)

    def createSegments(self):
        number_of_dictionaries = int(self.ui.number_of_segments.text())
        list_of_segments = [dict() for number in range(number_of_dictionaries)]
        for seg_index in range(number_of_dictionaries):
            if self.ui.process_table.item(seg_index, 1).text().isnumeric() == False:
                qtw.QMessageBox.critical(self, 'fail', f'You have to add an intger value in row {seg_index+1}')
                list_of_segments.clear()
                return
            
            elif int(self.ui.process_table.item(seg_index, 1).text()) <= 0:
                qtw.QMessageBox.critical(self, 'fail', 'You have to add a number greater than 0')
                list_of_segments.clear()
                return
            
            list_of_segments[seg_index]['name'] = self.ui.process_table.item(seg_index, 0).text()
            list_of_segments[seg_index]['size'] = int(self.ui.process_table.item(seg_index, 1).text())
            
        qtw.QMessageBox.information(self, 'success', 'Process is added sucessfully')

        return list_of_segments

    def _deallocate(self):
        if len(self.holes) == 0 and self.process_index == 0:
            qtw.QMessageBox.critical(self, 'fail', 'you have to add holes or processses first')
            return
        dea = deallocateMainWindow()
        widget1.addWidget(dea)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)
    index = 0


class deallocateMainWindow(qtw.QMainWindow, Ui_deallo):
    def __init__(self):
        super().__init__()

        self.ui = Ui_deallo()
        self.ui.setupUi(self)

        self.fil_new_table(new_dummy)
        self.fill_old_table(new_dummy)

        self.index = 0


        # deallocate from new
        self.ui.deallocate_new_button.clicked.connect(self.remove_from_new)

        # deallocate from old
        self.ui.deallocate_old_button.clicked.connect(self.remove_from_old)

        # back to main
        self.ui.back_button.clicked.connect(self.goBack)

    #button to update memory
        self.ui.memory_button2.clicked.connect(self.showMemory)

    # Sharnoby's Part
    def retranslateUiDraw(self, ChartWindow, text, i, length, myList, color):
        _translate = QtCore.QCoreApplication.translate
        self.ui.text.setHtml(_translate("ChartWindow", before_first_num1 + color + before_first_num2 + str(
            myList[i]['start']) + before_name + myList[i]['name'] + far_before_last_num + "15" + before_last_num + str(
            myList[i]['end']) + ending))

    def showMemory(self):
        if self.index == 0:
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
                'name': "Hole",
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
            self.index = 1
        else:
            myList = [
                {
                    'name': "Hole",
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
        for i in reversed(range(self.ui.verticalLayout_22.count())):
            self.ui.verticalLayout_22.itemAt(i).widget().setParent(None)
        #self.ui.verticalLayout_2.removeWidget(self.ui.text)

        start = 0
        for i in range(0, len(myList)):
            text = str(i)
            self.ui.text = qtw.QTextBrowser(self)
            length = myList[i]['end'] - myList[i]['start']
            self.ui.text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
            self.ui.text.setObjectName(text)
            self.ui.verticalLayout_22.addWidget(self.ui.text)
            start += length
            # qtw.setCentralWidget(self.ui.centralwidget)
            if myList[i]['name'][0] == 'P' or myList[i]['name'][0] == 'P':
                color = new_process
            elif myList[i]['name'][0] == 'H' or myList[i]['name'][0] == 'h':
                color = hole
            else:
                color = old_process
            self.retranslateUiDraw(self, text, i, length, myList, color)
            QtCore.QTimer.singleShot(0, self.ui.scrollAreaWidgetContents_22.adjustSize)


    def goBack(self):
        dea = TestMainWindow()
        widget1.addWidget(dea)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def remove_from_new(self):
        if self.ui.new_process_table.rowCount() > 0:
            current_row = self.ui.new_process_table.currentRow()
            if current_row < 0:
                qtw.QMessageBox.critical(self, 'warning', "please, select process")
            else:
                name_of_deleted = self.ui.new_process_table.item(current_row, 0).text()
                print(name_of_deleted)
                # send name_of_deleted to backend
                self.ui.new_process_table.removeRow(current_row)
                self.ui.deallocate_new_button.setEnabled(False)
                self.ui.deallocate_old_button.setEnabled(False)

    def fil_new_table(self, new_dummy):
        for i in range(len(new_dummy)):
            self.ui.new_process_table.insertRow(self.ui.new_process_table.rowCount())
        row = 0
        for process in new_dummy:
            self.ui.new_process_table.setItem(row, 0, qtw.QTableWidgetItem(process['name']))
            self.ui.new_process_table.setItem(row, 1, qtw.QTableWidgetItem(str(process['no_of_segments'])))
            row += 1

    def fill_old_table(self, new_dummy):
        for i in range(len(new_dummy)):
            self.ui.old_process_table.insertRow(self.ui.old_process_table.rowCount())
        row = 0
        for process in new_dummy:
            self.ui.old_process_table.setItem(row, 0, qtw.QTableWidgetItem(process['name']))
            # staring add.
            self.ui.old_process_table.setItem(row, 1, qtw.QTableWidgetItem(str(process['no_of_segments'])))
            # self.ui.old_process_table.setItem(row, 1, qtw.QTableWidgetItem(str(process['size'])))
            row += 1

    def remove_from_old(self):
        if self.ui.old_process_table.rowCount() > 0:
            current_row = self.ui.old_process_table.currentRow()
            if current_row < 0:
                qtw.QMessageBox.critical(self, 'warning', "please, select process")
            else:
                name_of_deleted = self.ui.old_process_table.item(current_row, 0).text()
                print(name_of_deleted)
                # send name_of_deleted to backend
                self.ui.old_process_table.removeRow(current_row)
                self.ui.deallocate_old_button.setEnabled(False)
                self.ui.deallocate_new_button.setEnabled(False)


# def _toMem(self):
    # show mem
    # def allocate_to_mem(self):
    # functions from backend


if __name__ == "__main__":
    app = qtw.QApplication([])
    widget1 = qtw.QStackedWidget()
    processes = TestMainWindow()
    widget1.addWidget(processes)
    widget1.show()
    app.exec_()
    # app = qtw.QApplication([])
    # widget = TestMainWindow()
    # widget.show()
    # app.exec_()