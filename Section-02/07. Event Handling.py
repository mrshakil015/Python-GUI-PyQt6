from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200,200, 700,400)
        self.setWindowTitle("PyQt6 Event Handling")
        self.setWindowIcon(QIcon('images/python.png'))

        self.create_widget()


    def create_widget(self):
        hbox = QHBoxLayout()
        btn = QPushButton("Change Text")
        btn.clicked.connect(self.clicked_btn)
        self.label = QLabel("Defalut Text")

        hbox.addWidget(btn)
        hbox.addWidget(self.label)

        self.setLayout(hbox)
    
    def clicked_btn(self):
        self.label.setText("Another Text")
        self.label.setStyleSheet('color: red')


app = QApplication(sys.argv)
Window = Window()
Window.show()
sys.exit(app.exec())