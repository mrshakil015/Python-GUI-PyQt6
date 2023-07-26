# Python-GUI-PyQt6

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
