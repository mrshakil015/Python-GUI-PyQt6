from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QApplication, QLabel
from input_widget import Ui_Form as Input_Form
from output_widget import Ui_Form as Output_Form

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

        self.chats_data = {  # Initialize chats_data as an empty dictionary
            "title": "",
            "chatlist": []
        }

        if self.chat_data:
            self.chats_data["title"] = self.chat_data["title"]
            self.chats_data["chatlist"] += self.chat_data["chatlist"]

        self.show_chats()

    def show_chats(self):
            # chat_title = self.chats_data.get("title")
            chat_list = self.chats_data.get("chatlist")
            for chat in chat_list:
                input_str = chat.get("input_str")
                input_widget = InputWidget(chat_obj=self.chat_object)
                input_widget.set_input_text(input_str)
                self.main_verticalLayout.addWidget(input_widget)

                out_str = chat.get("output_str")
                out_widget = OutWidget()
                out_widget.set_output_text(out_str)
                self.main_verticalLayout.addWidget(out_widget)

            spacerItem = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
            self.main_verticalLayout.addItem(spacerItem)
            self.setLayout(self.main_verticalLayout)


#     def show_chats(self):
#         chatlist = self.chats_data.get("chatlist")
#         for chat in chatlist:
#             input_str = chat.get("input_str")
#             input_widget = InputWidget(chat_obj=self.chat_object)
#             input_widget.set_input_text(input_str)
#             self.main_verticalLayout.addWidget(input_widget)

#             output_str = chat.get("output_str")
#             output_widget = OutputWidget()
#             output_widget.set_output_text(output_str)
#             # Set a fixed width for the output widgets (e.g., 600 pixels)
#             output_widget.setFixedWidth(600)

#             self.main_verticalLayout.addWidget(output_widget)

#         spacerItem = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
#         self.main_verticalLayout.addItem(spacerItem)
#         self.setLayout(self.main_verticalLayout)

#         # Adjust the size of the widget based on the display
#         screen_rect = QApplication.primaryScreen().availableGeometry()
#         self.resize(screen_rect.width() * 0.8, screen_rect.height() * 0.8)
#         self.move(screen_rect.width() * 0.1, screen_rect.height() * 0.1)

# class OutputWidget(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self.output_ui = Output_Form()
#         self.output_ui.setupUi(self)

#         self.output_text_browser = QTextBrowser()
#         self.output_text_browser.setOpenExternalLinks(True)  # To allow hyperlinks, if needed
#         self.output_text_browser.setStyleSheet("QTextBrowser { border: none; background-color: transparent; }")

#         self.output_ui.gridLayout.addWidget(self.output_text_browser, 0, 2, 1, 1)

#     def set_output_text(self, output_str):
#         self.output_text_browser.setPlainText(output_str)
