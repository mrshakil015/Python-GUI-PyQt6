from PyQt6.QtWidgets import QWidget

from home_widget import Ui_MainWindow

class HomeWindow(QWidget):
    def __init__(self):
        sueper().__init__()

        self.home_ui = Ui_MainWindow()
        self.home_ui.setupUi(self)