import sys
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QDialog, QApplication
from deallocate import Ui_deallo
from Process import Process
from Plotting import Ui_ChartWindow

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


class deallocateMainWindow(qtw.QMainWindow, Ui_deallo):
    def __init__(self):
        super().__init__()
        self.ui = Ui_deallo()
        self.ui.setupUi(self)

        self.fil_new_table(new_dummy)
        self.fill_old_table(new_dummy)

        # deallocate from new
        self.ui.deallocate_new_button.clicked.connect(self.remove_from_new)

        # deallocate from old
        self.ui.deallocate_old_button.clicked.connect(self.remove_from_old)

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


if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = deallocateMainWindow()
    widget.show()
    app.exec_()
