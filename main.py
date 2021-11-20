import sys
from random import randrange
from UI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class From(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setBrush(QColor(randrange(0, 256), randrange(0, 256), randrange(0, 256)))
        r = randrange(50, 250)
        qp.drawEllipse((300 - r) // 2, (300 - r) // 2, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = From()
    ex.show()
    sys.exit(app.exec_())