from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200,200, 700,400)
        self.setWindowTitle("Python GUI Development")
        self.setWindowIcon(QIcon('images/python.png'))

        vbox = QVBoxLayout()
        btn1 = QPushButton("Click One")
        btn2 = QPushButton("Click Two")
        btn3 = QPushButton("Click Three")
        btn4 = QPushButton("Click Four")
        btn5 = QPushButton("Click Five")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addWidget(btn5)
        vbox.addStretch(5)

        self.setLayout(vbox)
   


app = QApplication(sys.argv)
Window = Window()
Window.show()
sys.exit(app.exec())