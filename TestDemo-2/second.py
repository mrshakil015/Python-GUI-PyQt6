# Form implementation generated from reading ui file 'TestDemo-2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 650)
        MainWindow.setStyleSheet("#sidemenu {\n"
"background-color: #1b705b\n"
"}\n"
"\n"
"#sidemenu QPushButton{\n"
"border: none;\n"
"color: #fff;\n"
"text-align: left;\n"
"padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"#newconversation QFrame:hover{\n"
"background-color: #27a182;\n"
"color: black;\n"
"}\n"
"\n"
"#newconversation QFrame{\n"
"border: 2px solid #27a182;\n"
"}\n"
"#newconversation QFrame{\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"#chatlist{\n"
"background: #1b705b;\n"
"border:noe;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.sidemenu = QtWidgets.QWidget(parent=self.centralwidget)
        self.sidemenu.setMaximumSize(QtCore.QSize(220, 16777215))
        self.sidemenu.setObjectName("sidemenu")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.sidemenu)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.newconversation = QtWidgets.QFrame(parent=self.sidemenu)
        self.newconversation.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.newconversation.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.newconversation.setObjectName("newconversation")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.newconversation)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(parent=self.newconversation)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/plus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(18, 18))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout_4.addWidget(self.newconversation)
        self.frame_2 = QtWidgets.QFrame(parent=self.sidemenu)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chatlist = QtWidgets.QListView(parent=self.frame_2)
        self.chatlist.setObjectName("chatlist")
        self.verticalLayout_2.addWidget(self.chatlist)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.horizontalLayout_6.addWidget(self.sidemenu)
        self.mainwindow = QtWidgets.QWidget(parent=self.centralwidget)
        self.mainwindow.setObjectName("mainwindow")
        self.output = QtWidgets.QLabel(parent=self.mainwindow)
        self.output.setGeometry(QtCore.QRect(70, 260, 121, 16))
        self.output.setObjectName("output")
        self.horizontalLayout_6.addWidget(self.mainwindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "New Conversation"))
        self.output.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
