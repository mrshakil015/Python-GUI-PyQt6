import sys
from PyQt6.QtWidgets import QApplication
# from LibrarySystem import LibrarySystem
from PyQt6.QtWidgets import QMainWindow, QDialog
from MainWindow_GUI import Ui_MainWindow
from AddBook import Add_Dialog
from AddMember import Member_Dialog
from ViewBook import View_Dialog
from ViewMember import ViewMember_Dialog
import mysql.connector as mc

class LibrarySystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #--------Connect Signal------------
        self.toolButton_addbook.clicked.connect(self.add_book)
        self.toolButton_addmember.clicked.connect(self.add_member)
        self.toolButton_viewbook.clicked.connect(self.view_books)
        self.toolButton_viewmember.clicked.connect(self.view_member)
        self.lineEdit_bookid.returnPressed.connect(self.book_id)
        self.lineEdit_memberid.returnPressed.connect(self.member_id)


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

    def view_books(self):
        dialog = QDialog()
        ui = View_Dialog()
        ui.setupUi(dialog)
        dialog.exec()

    def view_member(self):
            dialog = QDialog()
            ui = ViewMember_Dialog()
            ui.setupUi(dialog)
            dialog.exec()

    #----------------Book Id Search Section-----------------

    import mysql.connector as mc  # Make sure you have the MySQL Connector Python library installed

    def book_id(self):
        id = self.lineEdit_bookid.text()

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="library_managemenet"
            )

            mycursor = mydb.cursor()
            query = "SELECT * FROM addbook_table WHERE id = '" + id + "'"
            mycursor.execute(query)

            result = mycursor.fetchall()

            if len(result) == 0:
                # Book ID not found in the database, show a message
                self.label_bookname.setText("<font color='red'>Book not found</font>")
                self.label_bookauthor.setText("")
            else:
                for row in result:
                    self.label_bookname.setText(row[0])
                    self.label_bookauthor.setText(row[2])

        except mc.Error as e:
            print("Error")


    #------------------Member id Section---------------------

    def member_id(self):
        id = self.lineEdit_memberid.text()

        try:
            mydb = mc.connect(
                host = "localhost",
                user="root",
                password="",
                database="library_managemenet"
            )

            mycursor = mydb.cursor()
            query = "SELECT * FROM addmember_table WHERE memberid = '"+id+"'"
            mycursor.execute(query)

            result = mycursor.fetchall()

            if len(result) == 0:
                # Book ID not found in the database, show a message
                self.label_membername.setText("<font color='red'>Member not found</font>")
                self.label_contactinfo.setText("")
            else:
                for row in result:
                    self.label_membername.setText(row[1])
                    self.label_contactinfo.setText(row[2])
        except mc.Error as e:
            print("Error")


     

app = QApplication(sys.argv)
library = LibrarySystem()

sys.exit(app.exec())
