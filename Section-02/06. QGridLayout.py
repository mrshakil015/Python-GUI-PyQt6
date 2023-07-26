from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200,200, 700,400)
        self.setWindowTitle("PyQt6 QGridLayout")
        self.setWindowIcon(QIcon('images/python.png'))


        grid = QGridLayout()


        btn1 = QPushButton("Click One")
        btn2 = QPushButton("Click Two")
        btn3 = QPushButton("Click Three")
        btn4 = QPushButton("Click Four")
        btn5 = QPushButton("Click Five")
        btn6 = QPushButton("Click Six")
        btn7 = QPushButton("Click Seven")
        btn8 = QPushButton("Click Eight")

        grid.addWidget(btn1,0,0)
        grid.addWidget(btn2,0,1)
        grid.addWidget(btn3,0,2)
        grid.addWidget(btn4,0,3)
        grid.addWidget(btn5,1,0)
        grid.addWidget(btn6,1,1)
        grid.addWidget(btn7,1,2)
        grid.addWidget(btn8,1,3)

        self.setLayout(grid)


app = QApplication(sys.argv)
Window = Window()
Window.show()
sys.exit(app.exec())