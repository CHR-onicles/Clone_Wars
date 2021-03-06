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

    def __init__(self, *args, color=None, font=None, **kwargs):
        super(LinkLabel, self).__init__(*args, **kwargs)
        self.color = color
        self.font = font

    def enterEvent(self, event):
        self.setStyleSheet(f'color: {self.color};'
                           f'font: {self.font};'
                           'text-decoration: underline;'
                           )

    def leaveEvent(self, event):
        self.setStyleSheet(f'color: {self.color};'
                           f'font: {self.font};'
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



class PasswordEdit(GlowingLineEdit):

    def __init__(self):
        super(PasswordEdit, self).__init__()
        self.visible_icon = QIcon('img/showf.png')
        self.hidden_icon = QIcon('img/hidef.png')

        self.setEchoMode(QLineEdit.Password)
        self.toggle_password_view = self.addAction(self.visible_icon, QLineEdit.TrailingPosition)
        self.toggle_password_view.triggered.connect(self.on_toggle_password_view)
        self.toggle_password_view.setVisible(False)
        self.is_password_visible = False
        self.textChanged.connect(self.on_text_changed)

    def on_toggle_password_view(self):
        if not self.is_password_visible:
            self.setEchoMode(QLineEdit.Normal)
            self.is_password_visible = True
            self.toggle_password_view.setIcon(self.hidden_icon)
        else:
            self.setEchoMode(QLineEdit.Password)
            self.is_password_visible = False
            self.toggle_password_view.setIcon(self.visible_icon)

    def on_text_changed(self):
        if self.text() == '':
            self.toggle_password_view.setVisible(False)
        else:
            self.toggle_password_view.setVisible(True)

