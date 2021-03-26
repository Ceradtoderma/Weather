from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import usin
import func
from datetime import datetime, timedelta


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.city = 'Ростов-на-Дону'
        self.state_resolution = 0
        self.ui = usin.Usin()
        self.ui.setupUI(self)
        self.weather_data = func.pars_weather_data(self.city)
        func.get_ico(self.weather_data)
        self.set_weather()
        self.set_week_weather()

        self.ui.tomorrow.setText((datetime.today() + timedelta(days=1)).strftime('%d %B'))
        self.ui.tomorrow.clicked.connect(lambda: self.set_weather(day=1))
        self.ui.aftertomorrow.setText((datetime.today() + timedelta(days=2)).strftime('%d %B'))
        self.ui.aftertomorrow.clicked.connect(lambda: self.set_weather(day=2))
        self.ui.afteraftertomorrow.setText((datetime.today() + timedelta(days=3)).strftime('%d %B'))
        self.ui.afteraftertomorrow.clicked.connect(lambda: self.set_weather(day=3))
        self.ui.more.clicked.connect(self.more)
        self.ui.change_city.clicked.connect(self.changecity)

        self.show()

    def set_weather(self, day=0):
        """
        Устанавливает нужные значения в окно графического интерфейса
        """
        param = func.get_param(self.weather_data, day)
        date, temp, dow, descr, f_l, cloudy, pressure, ico = param
        self.ui.date.setText(date)
        self.ui.icon.setPixmap(QtGui.QPixmap(f'icons/{ico}.png'))
        self.ui.Temp.setText(temp)
        self.ui.day_of_week.setText(dow)
        self.ui.Description.setText(descr)
        self.ui.feel_like.setText(f_l)
        self.ui.cloudy.setText(cloudy)
        self.ui.pressure.setText(pressure)

    def set_week_weather(self):
        for i in reversed(range(self.ui.gridLayout_more.count())):
            self.ui.gridLayout_more.itemAt(i).widget().setParent(None)

        cnt = 1
        for i in self.weather_data:
            font = QtGui.QFont()
            font.setFamily("Verdana")
            font.setPointSize(12)

            ico = i['ico']
            day = datetime.fromtimestamp(i["dt"])

            time_more = QtWidgets.QLabel(self.ui.frame)
            time_more.setText(day.strftime('%A').capitalize() + '\n' + day.strftime('%d.%m'))
            time_more.setFont(font)
            time_more.setAlignment(QtCore.Qt.AlignCenter)
            temp_more = QtWidgets.QLabel(self.ui.frame)
            temp_more.setText(str(round(i['temp'])) + '℃')
            temp_more.setFont(font)
            temp_more.setAlignment(QtCore.Qt.AlignCenter)
            icon_more = QtWidgets.QLabel(self.ui.frame)
            icon_more.setScaledContents(True)
            icon_more.setAlignment(QtCore.Qt.AlignCenter)
            icon_more.setPixmap(QtGui.QPixmap(f'icons/{ico}.png'))
            icon_more.setMaximumSize(QtCore.QSize(60, 60))
            icon_more.setMinimumSize(QtCore.QSize(60, 60))

            description_more = QtWidgets.QLabel(self.ui.frame)
            description_more.setText(i['descr'].replace(' ', '\n'))
            description_more.setAlignment(QtCore.Qt.AlignCenter)
            description_more.setFont(font)

            self.ui.gridLayout_more.addWidget(time_more, cnt, 0, 1, 1)
            self.ui.gridLayout_more.addWidget(temp_more, cnt, 1, 1, 1)
            self.ui.gridLayout_more.addWidget(icon_more, cnt, 2, 1, 1)
            self.ui.gridLayout_more.addWidget(description_more, cnt, 3, 1, 1)

            cnt += 1

    def more(self):
        if self.state_resolution == 0:
            self.resize(450, 840)
            self.state_resolution = 1
        else:
            self.resize(450, 381)
            self.state_resolution = 0

    def changecity(self):

        text, ok = QtWidgets.QInputDialog.getText(self, 'Смена города', 'Введите город:')

        if ok:
            self.city = text
            self.weather_data = func.pars_weather_data(self.city)
            func.get_ico(self.weather_data)
            self.set_weather()
            self.set_week_weather()


app = QtWidgets.QApplication([])

application = Window()

sys.exit(app.exec())
