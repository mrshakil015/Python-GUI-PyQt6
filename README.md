# Python-GUI-PyQt6

<details>
  <summary>Get Started with PyQt6 & Create Environment</summary>
PyQt is a set of Python bindings for building cross-platform applications, PyQt combines all the advantages of Qt and Python. With PyQt, you can include Qt libraries in python code, enabling you to write GUI applications in Python. In other words, we can say that PyQt allows you to access all the facilities provided by Qt through Python code. 
  
</br><b>Install Virtual Environment:</b>
  - virtualenv is considered as the virtual python environment builder which is used to create the multiple python virtual environment side by side. 
  - At first open <code>Visual Studio Code</code> then use following command to install virtual environment:
  ```python
pip install virtualenv
```
  - Once it is installed, we can create the new virtual environment into a folder as given below.
   ```python
python -m venv env
```
  - To activate the corresponding environment, use the following command on the Windows operating system.
  ```python
.\env\Scripts\activate
```
  - Then install the PyQt6 by using the following command:
  ```python
pip install pyqt6
pip install pyqt6-tools
```
  - Now Create your first Python file. In the below code used for the custom window:
  ```python
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200,200, 700,400)
        self.setWindowTitle("Python GUI Development")
        self.setWindowIcon(QIcon('images/python.png'))

app = QApplication(sys.argv)
Window = Window()
Window.show()
sys.exit(app.exec())
```
</details>

<details>
  <summary>Window Class Types</summary>

There are three different window type classes in PyQt6

- **QMainWindow:** The QMainWindow class provides a main application window  provides a framework for building an application's user interface. QMainWindow has its own layout to which we can add QToolBars, QDockWidgets, a QMenuBar, and a QStatusBar.
- **QDialog:** The QDialog class is the base class of dialog window and a dialog window is a top-level window mostly used for short-term tasks and brief communcation's with the user. QDialogs may be modal or modeless
- **QWidget:** The QWidget class is the base class of all user interface objects. The widget is an important point of the user interface: it receives the mouse, keyboard, and other events from the window system, and paints a representation of itself on the screen.

**Window Class Layout:**

* self.setGeometry(200,200, 700,400) - using for window size
* self.setWindowTitle("Python GUI Development") - using for title
* self.setWindowIcon(QIcon('images/python.png')) - using for set window icon
* self.setFixedHeight(400) - using for set the fixed height
* self.setFixedWidth(700) - using for set the fixed width
* self.setStyleSheet('background-color: red') - using for set the background color
* self.setWindowOpacity(0.5) - using for set window opacity

**Open QT Digner:**

* At First install- pip install pyqt6-tools
   ```python
  Then -->env-->Lib-->qt6 application-->Qt-->bin-->designer.exe
  ```
**Convert QT Digner UI file to py file:**

* Type text in terminal:
  ```python
  pyuic6 -x UIfilepath -o newfilename.py
  ```
</details>

<details>
  <summary>PyQt6 QLabel</summary>
QLabel is a widget that is used to display text or images. It is essentially a widget for showing a static text or an image on the user interface.


  + **Displaying Text:** QLabel is commonly used to show text on the GUI. It can display plain text, HTML-formatted text, or even rich text with formatting like fonts, colors, etc. This makes it useful for displaying instructions, labels, or any kind of textual information on the interface.
  + **Displaying Images:** QLabel can also be used to display images such as icons, logos, or pictures. It supports various image formats, and you can easily load and display images using this widget.
  + **Interaction:** Though QLabel is primarily used for displaying static content, it can be used to display clickable text or images as well. You can set up event handlers to respond to mouse clicks or other interactions on the QLabel.
  + **Alignment and Layout:** QLabel allows you to align the text or image within the widget, which is important for creating visually appealing interfaces. You can control the alignment horizontally and vertically, ensuring proper layout and presentation.
  + **Accessibility:** QLabel is useful for creating accessible interfaces since it can display text that can be read by screen readers, making your application more inclusive.
</details>

<details>
  <summary>PyQt6 QPushButton</summary>
  The push button, or command button, is perhaps the most commonly used widget in any graphical user interface. Push (click) a button to command the computer to perform some action, or to answer a question. Typical buttons are OK, Apply, Cancel, Close, Yes, No and Help.
  
  <br>**Specific Libraries:-**
  ```python
  from PyQt6.QtWidgets import QPushButton
  from PyQt6.QtGui import QFont, QIcon
  from PyQt6.QtCore import QSize 
  ```

**There are different methods that we can use in QPushButton.**
+ setText(): This method is used to assign text to the push button
+ setIcon(): This method is used to assign an icon to the push button
+ setGeometry(): This method is used for setting the x and y position, also width and height of the button.
+ setMenu(): This method is used for setting pop menu to the button.
 
</details>
