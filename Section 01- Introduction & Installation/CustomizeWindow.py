from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200,200, 700,400)
        self.setWindowTitle("Python GUI Development")
        self.setWindowIcon(QIcon('images/python.png'))
        
app = QApplication(sys.argv)
Window = Window()
Window.show()
sys.exit(app.exec())