from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200,200, 700,400)
        self.setWindowTitle("PyQt6 QHBoxLayout")
        self.setWindowIcon(QIcon('images/python.png'))

        #----Create QHBoxLayout Object-----
        hbox = QHBoxLayout()


        btn1 = QPushButton("Click One")
        btn2 = QPushButton("Click Two")
        btn3 = QPushButton("Click Three")
        btn4 = QPushButton("Click Four")
        btn5 = QPushButton("Click Five")

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)
        hbox.addWidget(btn5)
        hbox.addSpacing(100)

        self.setLayout(hbox)



app = QApplication(sys.argv)
Window = Window()
Window.show()
sys.exit(app.exec())