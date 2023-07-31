from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUiSecondWindow(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(900, 650)
        SecondWindow.setStyleSheet("#sidemenu {\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=SecondWindow)
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
        icon.addPixmap(QtGui.QPixmap("icons/plus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        self.SecondWindow = QtWidgets.QWidget(parent=self.centralwidget)
        self.SecondWindow.setObjectName("SecondWindow")
        self.output = QtWidgets.QLabel(parent=self.SecondWindow)
        self.output.setGeometry(QtCore.QRect(70, 260, 121, 16))
        self.output.setObjectName("output")
        self.horizontalLayout_6.addWidget(self.SecondWindow)
        SecondWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "SecondWindow"))
        self.pushButton.setText(_translate("SecondWindow", "New Conversation"))
        self.output.setText(_translate("SecondWindow", "TextLabel"))



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 650)
        MainWindow.setStyleSheet("#sidemenu {\n"
"background-color: #063d40\n"
"}\n"
"\n"
"#sidemenu QPushButton{\n"
"border: none;\n"
"color: #fff;\n"
"text-align: left;\n"
"padding: 5px;\n"
"\n"
"}\n"
"#menuframe{\n"
"border-top: 2px solid #0a676c;\n"
"}\n"
"#menuframe QFrame:hover,\n"
"#newconversation QFrame:hover{\n"
"background-color: #0a676c;\n"
"color: black;\n"
"}\n"
"\n"
"#newconversation QFrame{\n"
"border: 2px solid #0a676c;\n"
"}\n"
"#menuframe QFrame, #newconversation QFrame{\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"#chatlist{\n"
"background: #063d40;\n"
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
        icon.addPixmap(QtGui.QPixmap("icons/plus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        self.menuframe = QtWidgets.QFrame(parent=self.sidemenu)
        self.menuframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.menuframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menuframe.setObjectName("menuframe")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menuframe)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(parent=self.menuframe)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.frame_4)
        self.label.setMaximumSize(QtCore.QSize(18, 18))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/trash-2.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(parent=self.menuframe)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_2.setMaximumSize(QtCore.QSize(18, 18))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icons/settings.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame_5)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(parent=self.menuframe)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_3.setMaximumSize(QtCore.QSize(18, 18))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("icons/moon.svg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame_6)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(parent=self.menuframe)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_4.setMaximumSize(QtCore.QSize(18, 18))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("icons/log-out (1).svg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame_7)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        self.verticalLayout.addWidget(self.frame_7)
        self.verticalLayout_4.addWidget(self.menuframe)
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
        self.pushButton_2.setText(_translate("MainWindow", "Clear History"))
        self.pushButton_3.setText(_translate("MainWindow", "Setting"))
        self.pushButton_4.setText(_translate("MainWindow", "Mode"))
        self.pushButton_5.setText(_translate("MainWindow", "Log Out"))
        self.output.setText(_translate("MainWindow", ""))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.output.setText("")

        # Create a dictionary to map push buttons to their corresponding names
        self.push_buttons = {
            self.pushButton: "New Conversation",
            self.pushButton_2: "Clear History",
            self.pushButton_3: "Setting",
            self.pushButton_4: "Mode",
            self.pushButton_5: "Log Out"
        }

        # Connect the clicked signal of all push buttons to the same slot function
        for button in self.push_buttons:
            button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        # Get the sender object (the button that emitted the signal)
        sender = self.sender()

        # Get the name of the button from the dictionary and update the output label
        if sender in self.push_buttons:
            button_name = self.push_buttons[sender]
            self.output.setText(f"{button_name} clicked")

            # If the "Mode" button is clicked, open the TestDemo-2.py interface
            if button_name == "Mode":
                self.open_mode_interface()

    def open_mode_interface(self):
        # Create an instance of the TestDemo-2.py interface
        self.mode_interface = QtWidgets.QMainWindow()
        self.mode_ui = Ui_MainWindow()
        self.mode_ui.setupUi(self.mode_interface)

         # Hide the main window
        self.hide()

        # Show the TestDemo-2.py interface
        self.mode_interface.showMaximized()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()  # Create an instance of MainWindow
    window.showMaximized()  # Maximize the main window
    sys.exit(app.exec())
