from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200,200, 700,400)
        self.setWindowTitle("PyQt6 QLineEdit")
        self.setWindowIcon(QIcon('images/python.png'))

        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("Sanserif", 12))
        # line_edit.setText("Defalut Text")   # Write the defalut text
        line_edit.setPlaceholderText("Enter Your Text")
        # line_edit.setEnabled(False) # For enabled the line edit box
        line_edit.setMaxLength(5)



app = QApplication(sys.argv)
Window = Window()
Window.show()
sys.exit(app.exec())