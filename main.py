from PyQt5 import QtWidgets, QtGui
import sys
import usin
import func
from datetime import datetime, timedelta


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.city = 'Ростов-на-Дону'
        self.ui = usin.Usin()
        self.ui.setupUI(self)
        self.weather_data = func.pars_weather_data(self.city)
        func.get_ico(self.weather_data)
        self.set_weather()

        self.ui.tomorrow.setText((datetime.today() + timedelta(days=1)).strftime('%d %B'))
        self.ui.tomorrow.clicked.connect(lambda: self.set_weather(day=1))
        self.ui.aftertomorrow.setText((datetime.today() + timedelta(days=2)).strftime('%d %B'))
        self.ui.aftertomorrow.clicked.connect(lambda: self.set_weather(day=2))
        self.ui.afteraftertomorrow.setText((datetime.today() + timedelta(days=3)).strftime('%d %B'))
        self.ui.afteraftertomorrow.clicked.connect(lambda: self.set_weather(day=3))


        self.show()

    def set_weather(self, day=0):
        """
        Устанавливает нужные значения в окно графического интерфейса
        """
        param = func.get_param(self.weather_data, day)
        date, temp, dow, descr, f_l, cloudy, preasure, ico = param
        self.ui.date.setText(date)
        self.ui.icon.setPixmap(QtGui.QPixmap(f'icons/{ico}.png'))
        self.ui.Temp.setText(temp)
        self.ui.day_of_week.setText(dow)
        self.ui.Description.setText(descr)
        self.ui.feel_like.setText(f_l)
        self.ui.cloudy.setText(cloudy)
        self.ui.preasure.setText(preasure)

    def change_day(self):
        pass

app = QtWidgets.QApplication([])

application = Window()

sys.exit(app.exec())
