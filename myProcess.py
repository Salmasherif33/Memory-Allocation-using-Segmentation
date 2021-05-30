import sys
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QDialog, QApplication
from GUI_process import Ui_Form
from Process import Process
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

class ProcessMainWindow(qtw.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
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
        self.ui.memory_button.clicked.connect(self.openWindow)

    def openWindow(self):
        self.window = qtw.QMainWindow()
        self.ui = Ui_ChartWindow()
        #should add myList = memoryMap()
        self.ui.setupUi(self.window,myList)
        self.window.show()

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
        if int(self.ui.number_of_segments.text()) == 0:
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

    #def _toMem(self):
    #show mem
    #def allocate_to_mem(self):
    #functions from backend



if __name__ == "__main__":
    # app = qtw.QApplication([])
    # widget = qtw.QStackedWidget()
    # mainWindow = Inputs()
    # processes = ProcessMainWindow()
    # widget.addWidget(mainWindow)
    # widget.addWidget(processes)
    # widget.show()
    # app.exec_()

    app = qtw.QApplication([])
    widget = ProcessMainWindow()
    widget.show()
    app.exec_()
