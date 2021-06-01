import sys
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QDialog, QApplication
from GUI_process import Ui_Form
from Process import Process
from Plotting import Ui_ChartWindow
from myDeallocate import deallocateMainWindow
from window_test import Ui_Window_test


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

            for row in range(rowCount):
                start_adrr = self.ui.old_holes_tableWidget.item(row, 0).text()
                size = self.ui.old_holes_tableWidget.item(row, 1).text()
                hole = [start_adrr, size]
                self.holes.append(hole)
                # send to back

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
        if len(self.holes) <= 0:
            qtw.QMessageBox.critical(self, 'warning', "please, add holes first")
        elif int(self.ui.number_of_segments.text()) == 0:
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
            list_of_segments[seg_index]['name'] = self.ui.process_table.item(seg_index, 0).text()
            list_of_segments[seg_index]['size'] = int(self.ui.process_table.item(seg_index, 1).text())
        return list_of_segments

    def _deallocate(self):
        dea = deallocateMainWindow()
        widget1.addWidget(dea)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)
    # def _toMem(self):
    # show mem
    # def allocate_to_mem(self):
    # functions from backend


if __name__ == "__main__":
    app = qtw.QApplication([])
    widget1 = qtw.QStackedWidget()
    processes = TestMainWindow()
    deallocate = deallocateMainWindow()
    widget1.addWidget(processes)
    widget1.addWidget(deallocate)
    widget1.show()
    app.exec_()
    # app = qtw.QApplication([])
    # widget = TestMainWindow()
    # widget.show()
    # app.exec_()
