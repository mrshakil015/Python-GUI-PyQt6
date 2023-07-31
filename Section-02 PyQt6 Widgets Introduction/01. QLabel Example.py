from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200,200, 700,400)
        self.setWindowTitle("Python GUI Development")
        self.setWindowIcon(QIcon('images/python.png'))

        #----------For set the text-------------

        textlabel = QLabel(self)
        textlabel.setText("New Text is Here") #for write the text
        textlabel.move(100,10) #move the text
        textlabel.setFont(QFont("Sansrif", 10))
        textlabel.setStyleSheet('color:red') #set the label color
        
        #----------For load the image------------
        # from PyQt6.QtGui import QPixmap ---> labiarie

        imagelabel= QLabel(self)
        pixmap = QPixmap('./images/python.png')
        #Resize the image
        pixmap_sclaed = pixmap.scaled(100, 100)
        imagelabel.setPixmap(pixmap_sclaed)

          #----------For load the gif-----------
          # from PyQt6.QtGui import QMovie ---> labiarie

        giflabel = QLabel(self)
        movie = QMovie('./images/airplane.gif')
        movie.setSpeed(100)
        giflabel.setMovie(movie)
        movie.start()    
        giflabel.setGeometry(100, 100, 200, 200)
       

app = QApplication(sys.argv)
Window = Window()
Window.show()
sys.exit(app.exec())