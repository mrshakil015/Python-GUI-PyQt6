import json

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QListWidgetItem, QListView, \
    QStyledItemDelegate, QStyle, QWidget, QHBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QAbstractItemView, \
    QGridLayout, QLabel, QFrame, QVBoxLayout, QItemDelegate, QDialogButtonBox
from PyQt6.QtCore import pyqtSlot, QSize, QStringListModel, QPoint, Qt
from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem, QAction

from home_widget import Ui_MainWindow
from home_window import HomeWindow
from chat_window import ChatWindow
from login_window import LoginWindow
from connect_db import ConnectDB
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QTextCursor

import os
import fitz

import ai_chat

class CustomWidget(QWidget):
    ##Creath each chat in chat list
    def __init__(self, text,show_btn_flag, *args, **kwargs):
        super().__init__(*args,**kwargs)

        # Create layout for chat title
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5,0,0,0)

        #create icon widget fo chat title
        chat_icon = QIcon("Icons/bookmark.svg")
        chat_icon_btn = QPushButton(self)
        chat_icon_btn.setIcon(chat_icon)

        #create title widget to show title
        chat_title = QLineEdit(self)
        chat_title.setText(text)
        chat_title.setReadOnly(True)


        #create delete and edit buttons for chat title
        delete_btn = QPushButton(self)
        delete_btn.setIcon(QIcon("Icons/trash-2.svg"))

        edit_btn = QPushButton(self)
        edit_btn.setIcon(QIcon("Icons/edit.svg"))

        #style sheet for QPushButto in chat list
        style_str="""
            QPushButton{
                border: none;
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
        edit_btn.setStyleSheet(style_str)
        delete_btn.setStyleSheet(style_str)
        

        #check if be selected. if that hide delete
        if not show_btn_flag:
            delete_btn.hide()
            edit_btn.hide()
        
        #Add all the widgets of the chat title into layout

        layout.addWidget(chat_icon_btn)
        layout.addWidget(chat_title)
        layout.addWidget(edit_btn)
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
        self.clear_conversations_btn = self.ui.pushButton_2
        self.logout_btn = self.ui.pushButton_5
        self.profile_btn = self.ui.pushButton_9
        self.sidemenu = self.ui.sidemenu
        self.file_attatch_btn = self.ui.file_btn
        
        self.pdf_document = fitz.open()
        self.attached_pdf_path = None

        #Hide scrollbar of main scroll area
        self.main_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)


        
        #resize input frame and textEdit
        # self.message_input.setFixedHeight(24)
        # self.input_frame.setFixedHeight(42)


        #set data for main window when start app
        self.show_chatlist()
        self.show_home_window()

        #Set signal and slot
        self.send_message_btn.clicked.connect(self.get_response)
        self.new_chat_btn.clicked.connect(self.create_new_chat)
        self.clear_conversations_btn.clicked.connect(self.clear_conversations)
        self.logout_btn.clicked.connect(self.logout)
        self.profile_btn.clicked.connect(self.profile_section)
        self.file_attatch_btn.clicked.connect(self.attach_file)


#--------------Function for main window----------------
    #Extract pdf file information
    def attach_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Attach PDF File", "", "PDF Files (*.pdf);;All Files (*)"
        )
        if file_path:
            # Store the attached file path
            self.attached_pdf_path = file_path

            # Display the attached file name in the input section
            attached_file_text = f"Attached File: {os.path.basename(file_path)}"
            self.message_input.setPlainText(attached_file_text + "\n")

            # Automatically extract and display PDF information
            extracted_text = self.extract_pdf_info(file_path)
            
            # Clear existing text and insert extracted text
            self.message_input.setPlainText(extracted_text + "\n")
    
    def extract_pdf_info(self, pdf_path):
        try:
            doc = fitz.open(pdf_path)
            pdf_info = ""

            for page_num in range(doc.page_count):
                page = doc.load_page(page_num)
                pdf_info += page.get_text("text")

            doc.close()

            return pdf_info

        except Exception as e:
            error_message = f"Error extracting PDF information: {str(e)}"
            print(error_message)  # Print the error for debugging
            return error_message


    def get_response(self):
        message_input = self.message_input.toPlainText().strip()

        chat_db = self.connect_db.get_chat_data()

        if message_input:
            response_list = ai_chat.get_response(message_input)
            response_str = str(response_list)

            attached_pdf_info = None

            if self.attached_pdf_path:
                attached_pdf_info = self.extract_pdf_info(self.attached_pdf_path)
                response_str += f"\n[Attached PDF: {os.path.basename(self.attached_pdf_path)}]\n{attached_pdf_info}"
                self.attached_pdf_path = None  # Clear the attached PDF path

            if self.ui.chatlist.selectedIndexes():
                current_index = self.ui.chatlist.currentIndex()
                select_row = current_index.row()
                chat_db[select_row]["chatlist"].append({
                    "input_str": message_input,
                    "output_str": response_str,
                    "pdf_info": attached_pdf_info
                })
                chat_data = chat_db[select_row]
                self.connect_db.save_chat_data(chat_db)
                self.show_chat_window(chat_data)
            else:
                chat_data = {
                    "title": message_input,
                    "chatlist": [{
                        "input_str": message_input,
                        "output_str": response_str,
                        "pdf_info": attached_pdf_info
                    }]
                }
                chat_db.insert(0, chat_data)
                self.connect_db.save_chat_data(chat_db)
                self.show_chat_window(chat_data)
                self.show_chatlist(selected_index=0)

            self.message_input.clear()

        else:
            return

    #create profile section
    def profile_section(self):
        self.show_profile_window()
        self.show_chatlist(selected_index=None)

    #create a new chat
    def create_new_chat(self):
        self.show_home_window()
        self.show_chatlist(selected_index=None)

    #Delete all chat from chat list
    def clear_conversations(self):
        self.connect_db.delete_all_data()
        self.show_chatlist()

    # def get_response(self):
    #     message_input = self.message_input.toPlainText().strip()

    #     chat_db = self.connect_db.get_chat_data()

    #     if message_input:
    #         response_list = ai_chat.get_response(message_input)
    #         response_str = str(response_list)

    #         #Check if open a chat
    #         if self.ui.chatlist.selectedIndexes():
    #             #get current selected chat index
    #             current_index = self.ui.chatlist.currentIndex()
    #             select_row = current_index.row()
    #             chat_db[select_row]["chatlist"] +=[{"input_str": message_input,
    #                                                     "output_str": response_str}]
    #             chat_data = chat_db[select_row]

    #             #save data into database
    #             self.connect_db.save_chat_data(chat_db)
    #             #Reload window
    #             self.show_chat_window(chat_data)
    #         else:
    #             #create new chat and save it into database
    #             chat_data = {
    #                 "title": message_input,
    #                 "chatlist": [
    #                     {
    #                         "input_str": message_input,
    #                         "output_str": response_str
    #                     }
    #                 ]
                    
    #             }
    #             chat_db.insert(0, chat_data)
    #             self.connect_db.save_chat_data(chat_db)

    #             #reload window
    #             self.show_chat_window(chat_data)
    #             self.show_chatlist(selected_index=0)

    #         #Clear input
    #         self.message_input.clear()
    #     else:
    #         return


    #logout application
    def logout(self):
        self.close()


    def show_chatlist(self, selected_index=None):
        # Create QStrandardItemModel
        model = QStandardItemModel()
        self.ui.chatlist.setModel(model)

        # get chat title list from database
        chatlist = self.connect_db.get_chat_title_list()
        for chat in chatlist:
            item = QStandardItem()
            model.appendRow(item)

            index = item.index()
            index_text = index.row()
            if index_text == selected_index:
                show_btn_flag = True
                # set current item selected
                self.ui.chatlist.setCurrentIndex(index)
            else:
                show_btn_flag = False

            # create chat title widget
            widget = CustomWidget(chat, show_btn_flag)

            # set and show chat title in the list
            self.ui.chatlist.setIndexWidget(index, widget)

            # get pushbutton object in chat title widget
            operation_btns = widget.findChildren(QPushButton)

            # Connect signal and slot for buttons if there are enough elements
            if len(operation_btns) >= 3:
                edit_btn = operation_btns[2]
                edit_btn.clicked.connect(self.edit_chat)

                delete_btn = operation_btns[1]
                delete_btn.clicked.connect(self.delete_chat)


    #show a default window if ther is no chat is selected
    def show_home_window(self):
        grid_layout = self.clear_main_scroll_area()
        home_window = HomeWindow()
        grid_layout.addWidget(home_window)

    #show profile window
    def show_profile_window(self):
        grid_layout =self.clear_main_scroll_area()
        login_window = LoginWindow()
        grid_layout.addWidget(login_window)

    
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
    def edit_chat(self):
        current_index = self.ui.chatlist.currentIndex()
        current_chat = self.ui.chatlist.indexWidget(current_index)

        chat_title = current_chat.findChild(QLineEdit)

        # Get original chat title
        pre_chat_title = chat_title.text()

        chat_title.setReadOnly(False)
        chat_title_style = """
            QLineEdit {
                background:transparent;
                border: 1px solid #2563eb;
                color: #fff;
                font-size: 15px;
                padding-left: 2px;
            }
        """

        chat_title.setStyleSheet(chat_title_style)

        operation_btns = current_chat.findChildren(QPushButton)
        confirm_btn = operation_btns[2]
        cancel_btn = operation_btns[1]

        confirm_btn.setIcon(QIcon("static/icons/check-lg.svg"))
        cancel_btn.setIcon(QIcon("static/icons/x-lg.svg"))

        confirm_btn.clicked.disconnect()
        cancel_btn.clicked.disconnect()

        confirm_btn.clicked.connect(lambda: self.confirm_edit(chat_title))
        cancel_btn.clicked.connect(lambda: self.cancel_edit(pre_chat_title, chat_title))


    @pyqtSlot()
    def delete_chat(self):
        current_index = self.ui.chatlist.currentIndex()
        current_chat = self.ui.chatlist.indexWidget(current_index)

        chat_title = current_chat.findChild(QLineEdit)
        chat_title.setReadOnly(True)
        chat_title_text = chat_title.text()
        chat_title.setText(f'Delete "{chat_title_text}"?')
        chat_title_style = """
            QLineEdit {
                background:transparent;
                border: none;
                color: #fff;
                font-size: 15px;
                padding-left: 2px;
            }
        """

        chat_title.setStyleSheet(chat_title_style)

        operation_btns = current_chat.findChildren(QPushButton)
        chat_icon_btn = operation_btns[0]
        confirm_btn = operation_btns[2]
        cancel_btn = operation_btns[1]

        chat_icon_btn.setIcon(QIcon("Icons/trash-2.svg"))
        confirm_btn.setIcon(QIcon("Icons/check.svg"))
        cancel_btn.setIcon(QIcon("Icons/x.svg"))

        confirm_btn.clicked.disconnect()
        cancel_btn.clicked.disconnect()

        confirm_btn.clicked.connect(self.confirm_delete)
        cancel_btn.clicked.connect(self.cancel_delete)

    @pyqtSlot()
    def confirm_delete(self):
        current_index = self.ui.chatlist.currentIndex()
        index = current_index.row()
        chat_db = self.connect_db.get_chat_data()
        chat_db.pop(index)

        self.connect_db.save_chat_data(chat_db)
        self.show_home_window()
        self.show_chatlist()

    @pyqtSlot()
    def cancel_delete(self):
        self.on_chatlist_clicked()
    
    # @pyqtSlot()
    # def confirm_edit(self, chat_title):
    #     current_index = self.ui.chatlist.currentIndex().row()

    #     chat_db = self.connect_db.get_chat_data()
    #     chat_db[current_index]["title"] = chat_title.text()

    #     self.connect_db.save_chat_data(chat_db)
    #     self.on_chatlist_clicked()
    @pyqtSlot()
    def confirm_edit(self, chat_title):
        current_index = self.ui.chatlist.currentIndex().row()

        chat_db = self.connect_db.get_chat_data()
        chat_db[current_index]["title"] = chat_title.text()

        # Save the updated chat data
        self.connect_db.save_chat_data(chat_db)

        # Reload the chat list and display the updated chat title
        self.show_chatlist(selected_index=current_index)
        self.on_chatlist_clicked()

    @pyqtSlot()
    def cancel_edit(self, pre_chat_title, chat_title):
        chat_title.setText(pre_chat_title)
        self.on_chatlist_clicked()

    ## Functions for chat list ///////////////////////////////
    # Delete a chat form chat list
    def delete_chat_data(self):
        # Get current selected chat index
        selected_chat_index = self.ui.chatlist.currentIndex()
        index = selected_chat_index.row()

        # Delete the chat from database
        self.connect_db.delete_chat_data(index)

        # Reload window
        self.show_home_window()
        self.show_chatlist()

    # Function for clearing all the widgets in chat window when reload chat window
    def clear_main_scroll_area(self):
        # Get QGridLayout object from scroll area
        grid_layout = self.main_scrollArea.findChild(QGridLayout)
        grid_layout.setContentsMargins(0, 0, 0, 0)

        # Get all the objects in main chat window
        children_list = grid_layout.children()
        remove_widget_list = [QLabel, QPushButton, QFrame]
        for remove_widget in remove_widget_list:
            children_list += self.main_scrollArea.findChildren(remove_widget)

        # Delete all the found object
        for child in children_list:
            child.deleteLater()

        # Remove all the spacer items from the grid layout
        for row in range(grid_layout.rowCount()):
            for column in range(grid_layout.columnCount()):
                item = grid_layout.itemAtPosition(row, column)
                if item:
                    grid_layout.removeItem(item)

        return grid_layout

    # Signal and slot function for chat list(QListView)
    def on_chatlist_clicked(self):
        chatlist = []

         # Clear input when change chat
        self.message_input.clear()
        # Get select row
        current_index = self.ui.chatlist.currentIndex()
        select_row = current_index.row()

        # Get the count of chat list
        chat_models = self.ui.chatlist.model()
        chat_count = chat_models.rowCount()

        # Traverse chat list in window
        for i in range(chat_count):
            row_index = chat_models.index(i, 0)
            current_chat = self.ui.chatlist.indexWidget(row_index)
            chat_title = current_chat.findChild(QLineEdit)
            if chat_title:
                # Check if the chat state is waiting to delete
                if i == select_row and chat_title.text().startswith("Delete \""):
                    chatlist.append(chat_title.text().split('"')[1])
                else:
                    chatlist.append(chat_title.text())
            else:
                chatlist.append("")

        # Reload chat list
        for row, chat in enumerate(chatlist):
            index = chat_models.index(row, 0)
            # Check if the chat title is selected?
            if row == select_row:
                show_btn_flag = True
            else:
                show_btn_flag = False

            # Create chat title widget
            widget = CustomWidget(chat, show_btn_flag)

            # Set and show chat title in chat list(QListView)
            self.ui.chatlist.setIndexWidget(index, widget)

            # Get QPushButton object in  chat title widget
            operation_btn = widget.findChildren(QPushButton)

            # Connect signal and slot for buttons
            edit_btn = operation_btn[2]
            edit_btn.clicked.connect(self.edit_chat)

            delete_btn = operation_btn[1]
            delete_btn.clicked.connect(self.delete_chat)

        # Get the selected chat data and show it in main chat content window
        chat_db = self.connect_db.get_chat_data()
        chat_data = chat_db[select_row]
        self.show_chat_window(chat_data)




    

    




    