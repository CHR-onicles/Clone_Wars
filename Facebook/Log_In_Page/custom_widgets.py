from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



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

    color = QColor('#1877f2')
    signal_send_update = pyqtSignal()
    def __init__(self):
        super(GlowingLineEdit, self).__init__()
        self.cursor_visible = True
        self.timer = QTimer()
        self.timer.start(500)
        self.signal_send_update.connect(self.update)
        self.timer.timeout.connect(self.timer_slot)

    @pyqtSlot()
    def timer_slot(self):
        if self.cursor_visible:
            self.cursor_visible = False
        else:
            self.cursor_visible = True
        self.signal_send_update.emit()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.hasFocus():
            if self.cursor_visible:
                rect = self.cursorRect()
                painter = QPainter(self)
                new_rect = QRect(rect.x()+(rect.width()/2), rect.y(), rect.width()-(rect.width()*0.8),
                                 rect.height())
                painter.fillRect(new_rect, self.color)
            else:
                rect = self.cursorRect()
                painter = QPainter(self)
                new_rect = QRect(rect.x()+(rect.width()/2), rect.y(), rect.width()-(rect.width()*0.8),
                                 rect.height())
                painter.fillRect(new_rect, QColor('white'))

    def focusInEvent(self, event):
        effect = QGraphicsDropShadowEffect(self)
        effect.setOffset(0, 0)
        effect.setColor(self.color)
        effect.setBlurRadius(4)
        self.setGraphicsEffect(effect)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        effect = QGraphicsDropShadowEffect(self)
        effect.setEnabled(False)
        self.setGraphicsEffect(effect)
        super().focusOutEvent(event)
