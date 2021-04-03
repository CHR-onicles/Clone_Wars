import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from ui_mainwindow import UiMainWindow
import styles



class MainWindow(UiMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1200, 900)
        self.setWindowTitle('Facebook Clone')
        self.setWindowIcon(QIcon('img/fb_icon.ico'))
        self.setObjectName('mainwindow')
        self.setStyleSheet(styles.styles())
        self.setFocus()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


# TODO:--------------------------------------------------------------
#    - Resize echo mode characters - the oversized af dots.
#    - Create screen for wrong entry
