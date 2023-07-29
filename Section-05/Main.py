import sys
from PyQt6.QtWidgets import QApplication
# from LibrarySystem import LibrarySystem
from PyQt6.QtWidgets import QMainWindow, QDialog
from MainWindow_GUI import Ui_MainWindow
from AddBook import Add_Dialog
from AddMember import Member_Dialog

class LibrarySystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #--------Connect Signal------------
        self.toolButton_addbook.clicked.connect(self.add_book)
        self.toolButton_addmember.clicked.connect(self.add_member)


    def add_book(self):
        dialog = QDialog()
        ui = Add_Dialog()

        ui.setupUi(dialog)
        dialog.exec()
    
    def add_member(self):
        dialog = QDialog()
        ui = Member_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

app = QApplication(sys.argv)
library = LibrarySystem()

sys.exit(app.exec())
