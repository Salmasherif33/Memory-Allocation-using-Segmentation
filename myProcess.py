import sys
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QDialog, QApplication
from process import Ui_Form


class ProcessMainWindow(qtw.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # add segment to process_table
        self.ui.add_segment_button.clicked.connect(self._addRow)

        # add new process
        self.ui.add_process_button.clicked.connect(self._addNewProcess)

    def _addRow(self):
        no_of_segments = self.ui.number_of_segments.text()
        row_count = self.ui.process_table.rowCount()
        print(no_of_segments)
        if row_count < (int(no_of_segments)):
            self.ui.process_table.insertRow(self.ui.process_table.rowCount())
        else:
            qtw.QMessageBox.critical(self, 'fail', "all segments've been added")

    def _addNewProcess(self):
        self.clearScreen()

    def clearScreen(self):
        no_of_segments = self.ui.number_of_segments.text()
        if self.ui.process_table.rowCount() < int(no_of_segments):
            qtw.QMessageBox.critical(self, 'warning', "please, add all segments of this process")
        else:
            while self.ui.process_table.rowCount() > 0:
                self.ui.process_table.removeRow(self.ui.process_table.rowCount() - 1)

    # def _allocate(self):


if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = ProcessMainWindow()
    widget.show()
    app.exec_()
