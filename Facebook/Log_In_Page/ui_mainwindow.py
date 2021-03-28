from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from custom_widgets import QHSeparationLine, LinkLabel, GlowingLineEdit


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
        self.lbl_facebook.setObjectName('lbl_facebook')
        self.lbl_description = QLabel('Connect with friends and the world around you on Facebook.')
        self.lbl_description.setWordWrap(True)
        self.lbl_description.setObjectName('description')
        # </LEFT WIDGETS>

        # <RIGHT WIDGETS>
        self.entry_email = GlowingLineEdit()
        self.entry_email.setPlaceholderText('Email or Phone Number')
        self.entry_email.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.entry_password = GlowingLineEdit()
        self.entry_password.setPlaceholderText('Password')
        self.entry_password.setEchoMode(QLineEdit.Password)
        self.entry_password.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.btn_login = QPushButton('Log In')
        self.setObjectName('login')
        self.btn_login.setCursor(Qt.PointingHandCursor)

        self.lbl_forgot_password = LinkLabel('Forgot Password?')
        self.lbl_forgot_password.setStyleSheet('color: #1877f2; font: 10pt segoe UI;')
        self.lbl_forgot_password.setCursor(Qt.PointingHandCursor)
        self.lbl_forgot_password.setAlignment(Qt.AlignHCenter)

        self.hline = QHSeparationLine()
        self.hline.setStyleSheet('background-color: #d3d5d8;')

        self.btn_new_account = QPushButton('Create New Account')
        self.btn_new_account.setObjectName('new_account')
        self.btn_new_account.setCursor(Qt.PointingHandCursor)
        # </RIGHT WIDGETS>

    def layouts(self):
        self.main_layout = QHBoxLayout()

        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()
        self.new_account_layout = QHBoxLayout()

        # <LEFT LAYOUT>
        # self.left_layout.addStretch()
        self.left_layout.addWidget(self.lbl_facebook)
        self.left_layout.addSpacing(1)
        self.left_layout.addWidget(self.lbl_description)
        self.left_layout.addStretch()
        self.left_layout.setContentsMargins(50, 250, 50, 0)
        # </LEFT LAYOUT>

        # <NEW ACCOUNT LAYOUT>
        self.new_account_layout.addStretch()
        self.new_account_layout.addWidget(self.btn_new_account)
        self.new_account_layout.addStretch()
        # </NEW ACCOUNT LAYOUT>

        # <RIGHT LAYOUT>
        self.frame = QFrame()
        self.frame.setFixedWidth(500)
        self.frame_layout = QVBoxLayout()
        self.frame_layout.setContentsMargins(20, 20, 20, 30)
        self.frame_layout.setSpacing(20)
        self.frame_layout.addWidget(self.entry_email)
        self.frame_layout.addWidget(self.entry_password)
        self.frame_layout.addWidget(self.btn_login)
        self.frame_layout.addWidget(self.lbl_forgot_password)
        self.frame_layout.addWidget(self.hline)
        self.frame_layout.addLayout(self.new_account_layout)
        self.frame.setLayout(self.frame_layout)
        self.right_layout.addStretch()
        self.right_layout.addWidget(self.frame)
        self.right_layout.addStretch()
        self.right_layout.setContentsMargins(50, 0, 50, 0)
        # </RIGHT LAYOUT>


        self.main_layout.addLayout(self.left_layout, 60)
        self.main_layout.addLayout(self.right_layout, 40)
        self.setLayout(self.main_layout)
