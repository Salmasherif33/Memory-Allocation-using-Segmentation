import sys

from PyQt5 import QtWidgets

from window1 import Ui_InputWindow
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QDialog, QApplication
from myProcess import ProcessMainWindow


class Inputs(qtw.QMainWindow, Ui_InputWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_InputWindow()
        self.ui.setupUi(self)

        self.ui.size_doubleSpinBox.setMaximum(float('+inf'))
        self.ui.size_doubleSpinBox.setDecimals(5)
        self.ui.size_doubleSpinBox.clear()

        # button to add a hole
        self.ui.add_hole_pushButton.clicked.connect(self.add_hole_row)

        # button to delete the last row
        self.ui.delete_hole_pushButton.clicked.connect(self.delete_hole_row)

        # take mem size value
        memory_size = self.ui.size_doubleSpinBox.value()

        # button to add old processes
        self.ui.add_old_processes_pushButton.clicked.connect(self.add_old_processes)

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
            holes = []
            memory_size = self.ui.size_doubleSpinBox.value()

            for row in range(rowCount):
                start_adrr = self.ui.old_holes_tableWidget.item(row, 0).text()
                size = self.ui.old_holes_tableWidget.item(row, 1).text()
                hole = [start_adrr, size]
                holes.append(hole)

            qtw.QMessageBox.information(self, 'success', 'Holes are added sucessfully')
            print(holes)
            print(memory_size)
            widget.setCurrentIndex(widget.currentIndex()+1)
        except:
            qtw.QMessageBox.critical(self, 'fail', 'Something went wrong')


if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = qtw.QStackedWidget()
    mainWindow = Inputs()
    processes = ProcessMainWindow()
    widget.addWidget(mainWindow)
    widget.addWidget(processes)
    widget.show()
    app.exec_()

    # app = qtw.QApplication([])
    # w = Inputs()
    # w.show()
    # app.exec_()
    #
    # another choise
    # app = qtw.QApplication(sys.argv)
    # ex = Ui_InputWindow()
    # widget = QtWidgets.QMainWindow()
    # ex.setupUi(widget)
    # widget.show()
    # sys.exit(app.exec_())
