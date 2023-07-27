from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200,200, 400,200)
        self.setWindowTitle("PyQt6 QCheckBox")
        self.setWindowIcon(QIcon('./images/python.png'))

        hbox = QHBoxLayout()

        self.python_chk = QCheckBox("Python")
        self.python_chk.setIcon(QIcon("./images/python.png"))

        self.javascript_chk = QCheckBox("JavaScript")
        self.javascript_chk.setIcon(QIcon("./images/javascript.png"))

        self.java_chk = QCheckBox("Java")
        self.java_chk.setIcon(QIcon("./images/java.png"))

        self.label = QVBoxLayout("Hello")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        
        
        hbox.addWidget(self.python_chk)
        hbox.addWidget(self.javascript_chk)
        hbox.addWidget(self.java_chk)

        vbox.addLayout(hbox)

        self.setLayout(vbox)
        
app = QApplication(sys.argv)
Window = Window()
Window.show()
sys.exit(app.exec())