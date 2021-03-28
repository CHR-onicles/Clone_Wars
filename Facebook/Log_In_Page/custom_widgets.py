from PyQt5.QtWidgets import QFrame, QSizePolicy, QLabel, QLineEdit, QGraphicsDropShadowEffect
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor



class QHSeparationLine(QFrame):
    """
      Custom Class to create a horizontal separation line.
    """
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(1)
        self.setFixedHeight(1)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        return


class LinkLabel(QLabel):

    clicked = pyqtSignal()
    font_family = 'segoe UI'

    def enterEvent(self, event) -> None:
        self.setStyleSheet('color: #1877f2;'
                           'font-size: 10pt;'
                           f'font-family: {self.font_family};'
                           'text-decoration: underline;'
                           )

    def leaveEvent(self, event):
        self.setStyleSheet('color: #1877f2;'
                           'font-size: 10pt;'
                           f'font-family: {self.font_family};'
                           )

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)


class GlowingLineEdit(QLineEdit):

    def focusInEvent(self, event):
        effect = QGraphicsDropShadowEffect(self)
        effect.setOffset(0, 0)
        effect.setColor(QColor('#1877f2'))
        effect.setBlurRadius(4)
        self.setGraphicsEffect(effect)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        effect = QGraphicsDropShadowEffect(self)
        effect.setEnabled(False)
        self.setGraphicsEffect(effect)
        super().focusOutEvent(event)
