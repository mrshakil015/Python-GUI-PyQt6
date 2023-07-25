from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200,200, 700,400)
        self.setWindowTitle("Python GUI Development")
        self.setWindowIcon(QIcon('images/python.png'))
        # self.setFixedHeight(400)
        # self.setFixedWidth(700)
        # self.setStyleSheet('background-color: red')
        self.setWindowOpacity(0.5)
        
app = QApplication(sys.argv)
Window = Window()
Window.show()
sys.exit(app.exec())