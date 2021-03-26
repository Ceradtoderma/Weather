from PyQt5 import QtCore, QtGui, QtWidgets

class Usin(object):
    def setupUI(self, window):
        window.setGeometry(QtCore.QRect(500, 50, 450, 381))
        window.setMinimumSize(QtCore.QSize(450, 381))
        window.setMaximumSize(QtCore.QSize(450, 840))
        window.setWindowTitle('Погода')
        window.setWindowIcon(QtGui.QIcon('ico.png'))


        # Фрейм
        self.frame = QtWidgets.QFrame(window)
        self.frame.setGeometry(QtCore.QRect(0, 0, 450, 840))
        self.frame.setStyleSheet("background-color: rgba(4, 227, 220, 248);")

        # Кнопки

        self.tomorrow = QtWidgets.QPushButton('Завтра', window)
        self.tomorrow.setGeometry(QtCore.QRect(20, 310, 131, 31))
        self.aftertomorrow = QtWidgets.QPushButton('Послезавтра', window)
        self.aftertomorrow.setGeometry(QtCore.QRect(160, 310, 131, 31))
        self.afteraftertomorrow = QtWidgets.QPushButton('Послепослезавтра', window)
        self.afteraftertomorrow.setGeometry(QtCore.QRect(300, 310, 131, 31))
        self.more = QtWidgets.QPushButton('На неделю', window)
        self.more.setGeometry(QtCore.QRect(160, 350, 131, 31))
        self.change_city = QtWidgets.QPushButton(u'\u21cc', window)

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.change_city.setFont(font)
        self.change_city.setGeometry(QtCore.QRect(400, 10, 31, 31))

        # Лейблы
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.day_of_week = QtWidgets.QLabel('Понедельник', window)
        self.day_of_week.setGeometry(QtCore.QRect(20, 50, 151, 23))
        self.day_of_week.setFont(font)
        self.day_of_week.setAlignment(QtCore.Qt.AlignCenter)
        self.date = QtWidgets.QLabel('17 декабря', window)
        self.date.setGeometry(QtCore.QRect(300, 50, 111, 23))
        self.date.setFont(font)
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.icon = QtWidgets.QLabel(window)
        self.icon.setGeometry(QtCore.QRect(180, 20, 91, 81))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("02d@2x.png"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")

        self.layoutWidget = QtWidgets.QWidget(window)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 120, 411, 71))

        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.lbl_temp = QtWidgets.QLabel('Температура\nВоздуха', self.layoutWidget)
        self.lbl_temp.setFont(font)
        self.lbl_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_2.addWidget(self.lbl_temp, 0, 0, 1, 1)
        self.Description = QtWidgets.QLabel('Дождь', self.layoutWidget)
        self.Description.setFont(font)
        self.Description.setTextFormat(QtCore.Qt.AutoText)
        self.Description.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_2.addWidget(self.Description, 0, 2, 1, 1)
        self.Temp = QtWidgets.QLabel('+35', self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(26)
        self.Temp.setFont(font)
        self.Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_2.addWidget(self.Temp, 0, 1, 1, 1)

        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 220, 411, 71))

        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.lbl_feellike = QtWidgets.QLabel('Ощущается', self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lbl_feellike.setFont(font)
        self.lbl_feellike.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.lbl_feellike, 0, 0, 1, 1)

        self.lbl_pressure = QtWidgets.QLabel('Давление', self.layoutWidget1)
        self.lbl_pressure.setFont(font)
        self.lbl_pressure.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.lbl_pressure, 0, 1, 1, 1)

        self.lbl_cloudy = QtWidgets.QLabel('Облачность', self.layoutWidget1)
        self.lbl_cloudy.setFont(font)
        self.lbl_cloudy.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.lbl_cloudy, 0, 2, 1, 1)

        self.feel_like = QtWidgets.QLabel('+25', self.layoutWidget1)
        self.feel_like.setFont(font)
        self.feel_like.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.feel_like, 1, 0, 1, 1)

        self.pressure = QtWidgets.QLabel('720 мм.рт.ст', self.layoutWidget1)
        self.pressure.setFont(font)
        self.pressure.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.pressure, 1, 1, 1, 1)

        self.cloudy = QtWidgets.QLabel('58%', self.layoutWidget1)
        self.cloudy.setFont(font)
        self.cloudy.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.cloudy, 1, 2, 1, 1)

        self.layoutWidget_more = QtWidgets.QWidget(window)
        self.layoutWidget_more.setGeometry(QtCore.QRect(20, 380, 400, 440))

        self.gridLayout_more = QtWidgets.QGridLayout(self.layoutWidget_more)
        self.gridLayout_more.setContentsMargins(0, 0, 0, 0)
