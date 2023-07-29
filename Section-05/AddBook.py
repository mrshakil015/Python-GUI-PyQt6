# Form implementation generated from reading ui file 'c:\Users\MD. SHAMIM\Documents\GitHub\Python-GUI-PyQt6\Section-05\AddBook.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Add_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"background-color:  #00766d;\n"
"color: white\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_title = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_title.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_title.setFont(font)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.verticalLayout.addWidget(self.lineEdit_title)
        self.lineEdit_id = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_id.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_id.setFont(font)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.verticalLayout.addWidget(self.lineEdit_id)
        self.lineEdit_author = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_author.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_author.setFont(font)
        self.lineEdit_author.setObjectName("lineEdit_author")
        self.verticalLayout.addWidget(self.lineEdit_author)
        self.lineEdit_publisher = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_publisher.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_publisher.setFont(font)
        self.lineEdit_publisher.setObjectName("lineEdit_publisher")
        self.verticalLayout.addWidget(self.lineEdit_publisher)
        self.pushButton_addbook = QtWidgets.QPushButton(parent=Dialog)
        
         #connect signal
        self.pushButton_addbook.clicked.connect(self.insert_book)
        
        self.pushButton_addbook.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_addbook.setFont(font)
        self.pushButton_addbook.setStyleSheet("QPushButton {\n"
"background-color:  #00766d;\n"
"color: white\n"
"}")
        self.pushButton_addbook.setObjectName("pushButton_addbook")
        self.verticalLayout.addWidget(self.pushButton_addbook)
        self.label_result = QtWidgets.QLabel(parent=Dialog)
        self.label_result.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def insert_book(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user="root",
                password="",
                database="library_managemenet"
            )

            title = self.lineEdit_title.text()
            id = self.lineEdit_id.text()
            author = self.lineEdit_author.text()
            publisher = self.lineEdit_publisher.text()

            if title =="" or id =="" or author == "" or publisher =="":
                self.label_result.setText("Please Fill all fields")
                self.label_result.setStyleSheet("color: red")
                return
            
            mycursor = mydb.cursor()
            query = "INSERT INTO addbook_table (title, id, author, publisher) VALUES (%s, %s, %s, %s)"
            value = (title, id, author, publisher)
            mycursor.execute(query,value)

            mydb.commit()
            self.label_result.setText("Data added successfully")
            self.label_result.setStyleSheet("color: green")

            self.lineEdit_title.setText("")
            self.lineEdit_id.setText("")
            self.lineEdit_author.setText("")
            self.lineEdit_publisher.setText("")
                
        except mc.Error as e:
            self.label_result.setText("Failed to add Book")
            self.label_result.setStyleSheet("color: red")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Book"))
        self.label.setText(_translate("Dialog", "Insert Your Book "))
        self.lineEdit_title.setPlaceholderText(_translate("Dialog", "Please Enter Title"))
        self.lineEdit_id.setPlaceholderText(_translate("Dialog", "Please Enter ID"))
        self.lineEdit_author.setPlaceholderText(_translate("Dialog", "Please Enter Author"))
        self.lineEdit_publisher.setPlaceholderText(_translate("Dialog", "Please Enter Publisher"))
        self.pushButton_addbook.setText(_translate("Dialog", "Add Book"))
        self.label_result.setText(_translate("Dialog", ""))
