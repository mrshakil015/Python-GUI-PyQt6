import sys
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt6.QtGui import QColor, QBrush, QPainter, QPainterPath
from PyQt6.QtCore import Qt

class QPrism(QGraphicsItem):
    def __init__(self):
        super().__init__()
        self.baseColor = QColor(255, 0, 0)
        self.height = 100
        self.width = 100
        self.depth = 50

    def boundingRect(self):
        return self.shape().boundingRect()

    def shape(self):
        path = QPainterPath()
        path.moveTo(0, -self.depth)
        path.lineTo(self.width, -self.depth)
        path.lineTo(self.width / 2, 0)
        path.lineTo(0, -self.depth)
        path.moveTo(0, -self.depth)
        path.lineTo(0, self.height - self.depth)
        path.lineTo(self.width, self.height - self.depth)
        path.lineTo(self.width, 0)
        path.lineTo(self.width / 2, self.height - self.depth)
        path.lineTo(0, self.height - self.depth)
        return path

    def paint(self, painter, option, widget):
        painter.setPen(QColor(0, 0, 0))  # Use QColor to set the pen color
        painter.setBrush(QBrush(self.baseColor))
        painter.drawPath(self.shape())

def main():
    app = QApplication(sys.argv)
    scene = QGraphicsScene()
    prism = QPrism()
    scene.addItem(prism)
    view = QGraphicsView(scene)
    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
