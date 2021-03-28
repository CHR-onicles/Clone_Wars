from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from custom_widgets import QHSeparationLine, LinkLabel


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
        self.lbl_facebook.setStyleSheet('font: 20pt segoe UI; color: #1877f2;')
        self.lbl_description = QLabel('Connect with friends and the world\n around you on Facebook.')
        self.lbl_description.setStyleSheet('font: 15pt segoe UI;')
        # </LEFT WIDGETS>

        # <RIGHT WIDGETS>
        self.entry_email = QLineEdit()
        self.entry_email.setPlaceholderText('Email or Phone Number')

        self.entry_password = QLineEdit()
        self.entry_password.setPlaceholderText('Password')
        self.entry_password.setEchoMode(QLineEdit.Password)

        self.btn_login = QPushButton('Log In')

        self.lbl_forgot_password = LinkLabel('Forgot Password?')
        self.lbl_forgot_password.setStyleSheet('color: #1877f2; font: 9pt segoe UI;')

        self.hline = QHSeparationLine()

        self.btn_new_account = QPushButton('Create New Account')

        # </RIGHT WIDGETS>

    def layouts(self):
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
