from PyQt6.QtWidgets import QWidget, QVBoxLayout,QSpacerItem, QSizePolicy

from input_widget import Ui_Form as Input_Form
from output_widget import Ui_Form as Output_Form

class InputWidget(QWidget):
    def __init__(self, parent=None, chat_obj=None):
        sueper().__init__(parent)

        self.input_ui = Input_Form()
        self.input_ui.setupUi(self)

        self.chat_obj = chat_obj
        self.input_label = self.input_ui.label_2

    def set_input_text(self, input_str):
        self.input_label.setText(input_str)



class OutputWidget(QWidget):
    def __init__(self, parent=None):
        sueper().__init__(parent)

        self.output_ui = Output_Form()
        self.output_ui.setupUi(self)

        self.output_label = self.output_ui.label_2

    def set_output_text(self, output_str):
        self.output_label.setText(output_str)

class ChatWindow(QWidget):
    def __init__(self, parent=None, chat_obj=None, chat_data=None):
        super().__init__(parent)

        self.chat_object = chat_obj
        self.chat_data = chat_data


        self.main_verticalLayout = QVBoxLayout(self)
        self.main_verticalLayout.setContentsMargins(0,0,0,0)
        self.main_verticalLayout.setSpacing(0)
        self.main_verticalLayout.setObjectName("main_verticalLayout")

        self.style_str = """
            QPushButton,
            QLabel {
                border: none;
                padding: 5px;
            }

            QWidget {
                background: red;
            }
        
        """


        self.setStyleSheet(self.style_str)
        self.chat_data = {
            "title": "",
            "chat_list": []
        }

        if self.chat_data:
            self.chat_data["title"] = self.chat_data["title"]
            self.chats_data["title"] = self.chat_data["title"]
            self.chats_data["chat_list"] += self.chat_data["chat_list"]

        self.show_chats()

    def show_chats(self):
        chat_list = self.chats_data.get("chat_list")
        for chat in chat_list:
            input_str = chat.get("input_str")
            input_widget = InputWidget(chat_obj=self.chat_object)
            input_widget.set_input_text(input_str)
            self.main_verticalLayout.addWidget(input_widget)

            output_str = chat.get("output_str")
            output_widget = OutputWidget()
            output_widget.set_output_text(output_str)

            self.main_verticalLayout.addwidget(output_widget)

        spacerItem = QSpacerItem(20, 300, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.main_verticalLayout.addItem(spacerItem)
        self.setLayout(self.main_verticalLayout)
