import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from ui_mainwindow import UiMainWindow



class MainWindow(UiMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())