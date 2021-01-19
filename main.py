from PyQt5 import QtWidgets
import sys
import usin
import func

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.city = 'Ростов-на-Дону'
        self.ui = usin.Usin()
        self.ui.setupUI(self)
        self.set_weather()



        self.show()

    def set_weather(self):
        """
        Устанавливает нужные значения в окно графического интерфейса
        """
        param = func.get_param(self.city)
        date, temp, dow, descr, f_l, cloudy, preasure, ico = param
        self.ui.date.setText(date)
        # self.ui.icon.setPixmap(QtGui.QPixmap(f'icons/{ico}.png')) #TODO Нужна функция для получения иконок
        self.ui.Temp.setText(temp)
        self.ui.day_of_week.setText(dow)
        self.ui.Description.setText(descr)
        self.ui.feel_like.setText(f_l)
        self.ui.cloudy.setText(cloudy)
        self.ui.preasure.setText(preasure)


app = QtWidgets.QApplication([])

application = Window()

sys.exit(app.exec())
