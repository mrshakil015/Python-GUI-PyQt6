from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QApplication, QLabel
from PyQt6.QtGui import QPixmap
from input_widget import Ui_Form as Input_Form
from output_widget import Ui_Form as Output_Form
from markdown import markdown

class InputWidget(QWidget):
    def __init__(self, parent=None, chat_obj=None):
        super().__init__(parent)
        self.input_ui = Input_Form()
        self.input_ui.setupUi(self)

        self.chat_obj = chat_obj
        self.input_label = self.input_ui.label_2

    def set_input_text(self, input_str):
        self.input_label.setText(input_str)

class OutWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.output_ui = Output_Form()
        self.output_ui.setupUi(self)

        self.output_label = self.output_ui.label_2

        # Set QSizePolicy to Expanding for the label_2 widget
        self.output_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

    def set_output_text(self, out_str):
        self.output_label.setText(out_str)

class ChatWindow(QWidget):
    def __init__(self, parent=None, chat_obj=None, chat_data=None):
        super().__init__(parent)
        self.chat_object = chat_obj
        self.chat_data = chat_data

        self.main_verticalLayout = QVBoxLayout(self)
        self.main_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_verticalLayout.setSpacing(0)
        self.main_verticalLayout.setObjectName("main_verticalLayout")

        self.style_str = """
            QPushButton,
            QLabel {
                border: none;
                padding: 5px;
            }

            QWidget {
                background: transparent;
            }
        """

        self.setStyleSheet(self.style_str)

        self.chats_data = {
            "title": "",
            "chatlist": []
        }

        if self.chat_data:
            self.chats_data["title"] = self.chat_data["title"]
            self.chats_data["chatlist"] += self.chat_data["chatlist"]

        self.show_chats()

    def show_chats(self):
        chat_list = self.chats_data.get("chatlist")
        for chat in chat_list:
            input_str = chat.get("input_str")
            input_widget = InputWidget(chat_obj=self.chat_object)
            input_widget.set_input_text(input_str)
            self.main_verticalLayout.addWidget(input_widget)

            out_str = chat.get("output_str")
            out_widget = OutWidget()

            markdown_text = markdown(out_str, extensions=['markdown.extensions.extra', 'markdown.extensions.attr_list'])
            markdown_text = markdown_text.replace('<table>', '<table style="border: 1px solid white; padding: 10px; border-collapse: collapse;">')
            markdown_text = markdown_text.replace('<th>', '<th style="border: 1px solid white; padding: 10px;">')
            markdown_text = markdown_text.replace('<td>', '<td style="border: 1px solid white; padding: 10px;">')
            out_widget.set_output_text(markdown_text)
            self.main_verticalLayout.addWidget(out_widget)

            attached_pdf_info = chat.get("pdf_info")
            if attached_pdf_info:
                pdf_widget = OutWidget()
                pdf_widget.set_output_text(attached_pdf_info)
                self.main_verticalLayout.addWidget(pdf_widget)

        spacerItem = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.main_verticalLayout.addItem(spacerItem)
        self.setLayout(self.main_verticalLayout)

# class ChatWindow(QWidget):
#     def __init__(self, parent=None, chat_obj=None, chat_data=None):
#         super().__init__(parent)
#         self.chat_object = chat_obj
#         self.chat_data = chat_data

#         self.main_verticalLayout = QVBoxLayout(self)
#         self.main_verticalLayout.setContentsMargins(0, 0, 0, 0)
#         self.main_verticalLayout.setSpacing(0)
#         self.main_verticalLayout.setObjectName("main_verticalLayout")

#         self.style_str = """
#             QPushButton,
#             QLabel {
#                 border: none;
#                 padding: 5px;
#             }

#             QWidget {
#                 background: transparent;
#             }
        
#         """

#         self.setStyleSheet(self.style_str)

#         self.chats_data = {  # Initialize chats_data as an empty dictionary
#             "title": "",
#             "chatlist": []
#         }

#         if self.chat_data:
#             self.chats_data["title"] = self.chat_data["title"]
#             self.chats_data["chatlist"] += self.chat_data["chatlist"]

#         self.show_chats()
#     def show_chats(self):
#             # chat_title = self.chats_data.get("title")
#             chat_list = self.chats_data.get("chatlist")
#             for chat in chat_list:
#                 input_str = chat.get("input_str")
#                 input_widget = InputWidget(chat_obj=self.chat_object)
#                 input_widget.set_input_text(input_str)
#                 self.main_verticalLayout.addWidget(input_widget)

#                 out_str = chat.get("output_str")
#                 out_widget = OutWidget()
#                 # markdown_text = markdown(out_str, extensions=['markdown.extensions.extra', 'markdown.extensions.tables'])
                
#                 markdown_text = markdown(out_str, extensions=['markdown.extensions.extra', 'markdown.extensions.attr_list'])
                
#                 # Add the custom attributes for the table, th, and td elements
#                 markdown_text = markdown_text.replace('<table>', '<table style="border: 1px solid white; padding: 10px; border-collapse: collapse;">')
#                 markdown_text = markdown_text.replace('<th>', '<th style="border: 1px solid white; padding: 10px;">')
#                 markdown_text = markdown_text.replace('<td>', '<td style="border: 1px solid white; padding: 10px;">')
#                 out_widget.set_output_text(markdown_text)
#                 self.main_verticalLayout.addWidget(out_widget)

#                 # out_str = chat.get("output_str")
#                 # out_widget = OutWidget()
#                 # out_widget.set_output_text(out_str)
#                 # self.main_verticalLayout.addWidget(out_widget)

#             spacerItem = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
#             self.main_verticalLayout.addItem(spacerItem)
#             self.setLayout(self.main_verticalLayout)

    # def show_chats(self):
    #     chat_list = self.chats_data.get("chatlist")
    #     for chat in chat_list:
    #         input_str = chat.get("input_str")
    #         input_widget = InputWidget(chat_obj=self.chat_object)
    #         input_widget.set_input_text(input_str)
    #         self.main_verticalLayout.addWidget(input_widget)

    #         out_str = chat.get("output_str")
    #         out_widget = OutWidget()

    #         # Check if the output is an image
    #         if out_str.startswith("[Image "):
    #             image_path = out_str[len("[Image "):-1]  # Extract the image path from the output string
    #             image_widget = QLabel()
    #             pixmap = QPixmap(image_path)
    #             if not pixmap.isNull():
    #                 image_widget.setPixmap(pixmap.scaledToWidth(400))  # Adjust the width as needed
    #                 self.main_verticalLayout.addWidget(image_widget)
    #         else:
    #             # If it's not an image, treat it as regular text and convert any markdown in the output
    #             markdown_text = markdown(out_str, extensions=['markdown.extensions.extra', 'markdown.extensions.tables'])
    #             out_widget.set_output_text(markdown_text)
    #             self.main_verticalLayout.addWidget(out_widget)

    #     spacerItem = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
    #     self.main_verticalLayout.addItem(spacerItem)
    #     self.setLayout(self.main_verticalLayout)

    

