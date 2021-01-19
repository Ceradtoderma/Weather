from PyQt5 import QtWidgets
import sys
import usin
import func

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = usin.Usin()
        self.ui.setupUI(self)


        self.show()


app = QtWidgets.QApplication([])

application = Window()

sys.exit(app.exec())
