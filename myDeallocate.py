import sys
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QDialog, QApplication
from deallocate import Ui_deallo
from Process import Process
from Plotting import Ui_ChartWindow


class deallocateMainWindow(qtw.QMainWindow, Ui_deallo):
    def __init__(self):
        super().__init__()
        self.ui = Ui_deallo()
        self.ui.setupUi(self)

        self.fil_table()

        # deallocate from new
        self.ui.deallocate_new_button.clicked.connect(self.remove_from_new)

    def remove_from_new(self):
        if self.ui.new_process_table.rowCount() > 0:
            current_row = self.ui.new_process_table.currentRow()
            self.ui.new_process_table.removeRow(current_row)

    def fil_table(self):
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
        for i in range(len(new_dummy)):
            self.ui.new_process_table.insertRow(self.ui.new_process_table.rowCount())
        row = 0
        for process in new_dummy:
            self.ui.new_process_table.setItem(row, 0, qtw.QTableWidgetItem(process['name']))
            self.ui.new_process_table.setItem(row, 1, qtw.QTableWidgetItem(str(process['no_of_segments'])))
            row += 1


if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = deallocateMainWindow()
    widget.show()
    app.exec_()
