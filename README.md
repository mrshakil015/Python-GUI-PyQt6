# Python-GUI-PyQt6

## Window Class Types

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
