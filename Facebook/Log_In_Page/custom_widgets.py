from PyQt5.QtWidgets import QFrame, QSizePolicy, QLabel
from PyQt5.QtCore import pyqtSignal



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

    def enterEvent(self, event) -> None:
        self.setStyleSheet(
            """
            QLabel {
                color: #1877f2;
                font: 10pt segoe UI;
                text-decoration: underline;
            }
            """
        )

    def leaveEvent(self, event):
        self.setStyleSheet(
            """
            QLabel {
                color: #1877f2;
                font: 10pt segoe UI;
            }
            """
        )

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)