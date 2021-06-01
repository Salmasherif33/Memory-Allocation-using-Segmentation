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
    widget = deallocateMainWindow()
    widget.show()
    app.exec_()
