import json

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QListWidgetItem, QListView, \
    QStyledItemDelegate, QStyle, QWidget, QHBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QAbstractItemView, \
    QGridLayout, QLabel, QFrame, QVBoxLayout, QItemDelegate, QDialogButtonBox
from PyQt6.QtCore import pyqtSlot, QSize, QStringListModel, QPoint, Qt
from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem, QAction

from home_widget import Ui_MainWindow
from home_window import HomeWindow
from chat_window import ChatWindow
from connect_db import ConnectDB

class CustomWidget(QWidget):
    ##Creath each chat in chat list
    def __init__(self, text,show_btn_flag, *args, **kwargs):
        super().__init__(*args,**kwargs)

        # Create layout for chat title
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5,0,0,0)

        #create icon widget fo chat title
        chat_icon = QIcon("Icons/lock.svg")
        chat_icon_btn = QPushButton(self)
        chat_icon_btn.setIcon(chat_icon)

        #create title widget to show title
        chat_title = QLineEdit(self)
        chat_title.setText(text)
        chat_title.setReadOnly(True)

        #create delete and edit buttons for chat title
        delete_btn = QpushButton(self)
        delete_btn.setIcon(QIcon("Icons/moon.svg"))

        #style sheet for QPushButto in chat list
        style_str="""
            QPushButton{
                border: non;
                max-width: 20px;
                max-height: 20px;
                background: transparent;
            }
        """

        #style sheet for QLineEdit in chat list
        chat_title_style_str = """
            QLineEdit {
                background: transparent;
                border: none;
                color: #fff;
                font-size: 15px;
                padding-left: 2px;
            }
        """


        chat_title.setStyleSheet(chat_title_style_str)
        chat_icon_btn.setStyleSheet(style_str)
        delete_btn.setStyleSheet(style_str)
        

        #check if be selected. if that hide delete
        if not show_btn_flag:
            delete_btn.hide()
        
        #Add all the widgets of the chat title into layout

        layout.addWidget(chat_icon_btn)
        layout.addWidget(chat_title)
        layout.addWidget(delete_btn)

        


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Initialize of the main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Instantiate the database object
        self.connect_db = ConnectDB()

        #Get objects from main window
        self.message_input = self.ui.input_textEdit
        self.input_frame = self.ui.input_frame
        self.new_chat_btn = self.ui.pushButton
        self.send_message_btn = self.ui.send_btn
        self.main_scrollArea = self.ui.main_scrollArea
        self.clear_conversations_btn = self.pushButton_2
        self.logout_btn = self.ui.pushButton_5

        #Hide scrollbar of main scroll area
        self.main_scrollArea.setVerticalScrollBarPolicy(1)
        
        #resize input frame and textEdit
        self.message_input.setFixedHeight(24)
        self.input_frame.setFixedHeight(42)


        #set data for main window when start app
        self.show_chat_list()
        self.show_home_window()

        #Set signal and slot
        self.send_message_btn.clicked.connect(self.get_response)
        self.new_chat_btn.clicked.connect(self.create_new_chat)
        self.clear_conversations_btn.clicked.connect(self.clear_conversations)
        self.logout_btn.clicked.connect(self.logout)


#--------------Function for main window----------------
    #create a new chat
    def create_new_chat(self):
        self.show_home_window()
        self.show_chat_list(selected_index=None)

    #Delete all chat from chat list
    def clear_conversations(self):
        self.connect_db.delete_all_data()
        self.show_chat_list()

    #Get response
    def get_response(self):
        message_input = self.message_input.toPlainText.strip()
        chat_db = self.connect_db.get_chat_data()

        if message_input:
            response_list = ai_chat.get_response(message_input)
            response_str = "\n".jon(response_list)

            #Check if open a chat
            if self.ui.chatlist.selectedIndexes():
                #get current selected chat index
                current_index = self.ui.chatlist.currentIndex()
                select_row = current_index.row()
                chat_db[select_row]["chat_list"] +=[{"input_str": message_input,
                                                        "output_str": response_str}]
                chat_data = chat_db[select_row]

                #save data into database
                self.connect_db.save_chat_data(chat_db)
                self.show_chat_window(chat_data)

    #logout application
    def logout(self):
        self.close()


    #show chat title list
    def show_chat_list(self, selected_index=None):
        #Create QStrandardItemModel
        model = QStandardItemModel()
        self.ui.chatlist.setModel(model)
        #get chat title list from database
        chat_list = self.connect_db.get_chat_title_list()
        for chat in chat_list:
            item = QStandardItem()
            model.appendRow(item)

            index = intem.index()
            index_text = index.row()
            if index_text == selected_index:
                show_btn_flag = True
                #set current item selected
                self.ui.chatlist.setCurrentIndex(index)
            else:
                show_btn_flag = False
            
            #create chat title widget
            widget = CustomWidget(chat, show_btn_flag)

            #set and show chat title in the list
            self.ui.chatlist.setIndexWidget(index, widget)

            #get pushbutton object in chat title widget
            operation_btns = widget.findChildren(QPushButton)

            #connect signal and slog for buttons
            delete_btn = operation_btns[1]
            delete_btn.clicked.connect(self.delete_chat)

    #show a default window if ther is no chat is selected
    def show_home_window(self):
        grid_layout = self.clear_main_scroll_area()
        home_window = HomeWindow()
        grid_layout.addWidget(home_window)
    
    #show one chat data in main chat window
    def show_chat_window(self, chat_data):
        grid_layout = self.clear_main_scroll_area()
        #show new message
        chat_window = ChatWindow(chat_obj=self.message_input, chat_data=chat_data)
        grid_layout.addWidget(chat_window)

    #clear all widgets in chat window when reload chat window
    def clear_main_scroll_area(self):
        #get Qgridlayout object from scroll area
        grid_layout = self.main_scrollArea.findChild(QGridLayout)
        grid_layout.setContentsMargins(0,0,0,0)

        #Get all the objects in main chat window
        children_list = grid_layout.children()
        remove_widget_list = [QLabel, QPushButton, QFrame]
        for remove_widget in remove_widget_list:
            children_list += self.main_scrollArea.findChildren(remove_widget)

        #Delete all the found object
        for child in children_list:
            child.deleteLater()

        #Remove all the spacer item from the gride layout
        for row in range(grid_layout.rowCount()):
            for column in  range(grid_layout.columnCount()):
                item = grid_layout.itemAtPosition(row, column)
                if item:
                    grid_layout.removeItem(item)
        return grid_layout


@pyqtSlot()
def delete_chat(self):
    pass

    

    




    