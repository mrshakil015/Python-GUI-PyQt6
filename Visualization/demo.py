import sys
import js2py

from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

widget = QWidget()
widget.setWindowTitle("PyQt6 with JavaScript")

def myFunction():
  print("Hello from JavaScript!")

jsCode = """
function myFunction() {
  console.log("Hello from JavaScript!");
}
"""

js = js2py.eval_js(jsCode)
js.myFunction()

widget.show()

app.exec()
