from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton,QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize  # used for resize the icon size
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
      
        self.setGeometry(200,200, 300,200)
        self.setWindowTitle("PyQt6 QRadioButton")
        self.setWindowIcon(QIcon('../images/python.png'))

        self.create_radio()
    
    def create_radio(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        rad1 = QRadioButton("JavaScript")
        rad1.setIcon(QIcon("../images/javascript.png"))
        rad1.setIconSize(QSize(20,20))  # resize the icon size
        rad1.setChecked(True)   # for by-deafult checked
        rad1.toggled.connect(self.radio_selected)
        hbox.addWidget(rad1)
        

        rad2 = QRadioButton("Python")
        rad2.setIcon(QIcon("../images/python.png"))
        rad2.setIconSize(QSize(20,20))  # resize the icon size
        rad2.toggled.connect(self.radio_selected)
        hbox.addWidget(rad2)

        rad3 = QRadioButton("Java")
        rad3.setIcon(QIcon("../images/java.png"))
        rad3.setIconSize(QSize(20,20))  # resize the icon size
        rad3.toggled.connect(self.radio_selected)
        hbox.addWidget(rad3)

        self.label = QLabel("")
        
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)


        
        self.setLayout(vbox)


    def radio_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.label.setText("You have selected: {}".format(radio_btn.text()))

app = QApplication(sys.argv)
Window = Window()
Window.show()
sys.exit(app.exec())