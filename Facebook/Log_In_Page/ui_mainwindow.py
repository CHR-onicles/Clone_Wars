from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *




class UiMainWindow(QWidget):

    def __init__(self):
        super(UiMainWindow, self).__init__()

        self.ui_components()

    def ui_components(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        # <LEFT WIDGETS>
        self.lbl_facebook = QLabel('facebook')
        self.lbl_description = QLabel('Connect with friends and the world\n around you on Facebook.')
        # </LEFT WIDGETS>

        # <RIGHT WIDGETS>
        self.entry_email = QLineEdit()
        self.entry_email.setPlaceholderText('Email or Phone Number')

        self.entry_password = QLineEdit()
        self.entry_password.setPlaceholderText('Password')
        self.entry_password.setEchoMode(QLineEdit.Password)

        self.btn_login = QPushButton('Log In')

        # </RIGHT WIDGETS>

    def layouts(self):
        pass
