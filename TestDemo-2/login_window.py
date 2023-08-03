from PyQt6.QtWidgets import QWidget

from login import Ui_Form as Login_Form


class LoginWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.login_ui = Login_Form()
        self.login_ui.setupUi(self)