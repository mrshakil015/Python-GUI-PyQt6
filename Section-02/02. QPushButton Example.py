from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200,200, 700,400)
        self.setWindowTitle("PyQt6 QPushButton")
        self.setWindowIcon(QIcon('images/python.png'))

        self.create_button()

    #--------Create Button-----------
    #   from PyQt6.QtWidgets import QPushButton

    def create_button(self):
        btn =  QPushButton("Click", self)
        btn.setGeometry(100,100, 110,50) #Resize the button
        btn.setFont(QFont("Times", 14, QFont.Weight.Bold))  #Set Font style --> from PyQt6.QtGui import QFont
        btn.setIcon(QIcon("./images/python.png"))   # Set Icon --> from PyQt6.QtGui import QIcon
        btn.setIconSize(QSize(36,36))   # Resize the icon --> from PyQt6.QtCore import QSize


        #------Button Click Popup Menu----------
        menu = QMenu()
        menu.setFont(QFont("Times", 10, QFont.Weight.Bold))
        # Set popup menu color
        menu.setStyleSheet("background-color: #0a676c;")
        # Add popup menu elements
        menu.addAction("Cut")
        menu.addAction("Copy")
        menu.addAction("Paste")
        btn.setMenu(menu)








app = QApplication(sys.argv)
Window = Window()
Window.show()
sys.exit(app.exec())