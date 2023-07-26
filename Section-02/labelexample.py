from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200,200, 700,400)
        self.setWindowTitle("Python GUI Development")
        self.setWindowIcon(QIcon('images/python.png'))

        #----------For set the text-------------

        label = QLabel("Python GUI Development", self)
        label.setText("New Text is Here") #for write the text
        label.move(10,10) #move the text
        label.setFont(QFont("Sansrif", 10))
        label.setStyleSheet('color:red') #set the label color
        
        #----------For set the image------------

        label2= QLabel(self)
        pixmap = QPixmap('./images/python.png')
        #Resize the image
        pixmap_sclaed = pixmap.scaled(100, 100)
        label2.setPixmap(pixmap_sclaed)
        
        
       


app = QApplication(sys.argv)
Window = Window()
Window.show()
sys.exit(app.exec())