from PyQt6.QtWidgets import QMainWindow, QDialog
from MainGUI import Ui_MainWindow
from AddBook import Add_Dialog

class LibrarySystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #--------Connect Signal------------
        self.toolButton_addbook.clicked.connect(self.add_book)



    def add_book(self):
        dialog = QDialog()
        ui = Add_Dialog()

        ui.setupUi(dialog)
        dialog.exec()