import requests
from datetime import datetime
import locale
import os


locale.setlocale(locale.LC_ALL, "ru")
API_WEATHER_KEY = 'fc3837d82e69a8bea3f8c2a0f1e68643'
# city = 'Ростов-на-Дону'
city = 'asdasd'

def get_param(weather_data, day):
    """
    :return: Кортеж параметров в виде строк
    """
    date = str(weather_data[day]['date'])
    temp = str(round(weather_data[day]['temp'])) + '℃'
    dow = str(weather_data[day]['dow'])
    descr = str(weather_data[day]['descr']).replace(' ', '\n').capitalize()
    f_l = str(round(weather_data[day]['f_l'])) + '℃'
    cloudy = str(weather_data[day]['cloudy']) + '%'
    pressure = str(round(weather_data[day]['pressure'] / 1.333)) + '\nмм.рт.ст.'
    ico = str(weather_data[day]['ico'])

    param = (date, temp, dow, descr, f_l, cloudy, pressure, ico)
    return param


def pars_weather_data(city):
    lat, lon = get_coord(city)
    responce = get_weather_data(lat, lon)
    weather_data = []
    cnt = 0
    for i in responce['daily']:
        dt = i['dt']
        weather_data.append([])
        weather_data[cnt] = {}
        weather_data[cnt]['dt'] = i['dt']
        weather_data[cnt]['date'] = datetime.fromtimestamp(dt).strftime('%B, %d')
        weather_data[cnt]['temp'] = i['temp']['day']
        weather_data[cnt]['dow'] = datetime.fromtimestamp(dt).strftime('%A').capitalize()
        weather_data[cnt]['descr'] = i['weather'][0]['description']
        weather_data[cnt]['f_l'] = i['feels_like']['day']
        weather_data[cnt]['cloudy'] = i['clouds']
        weather_data[cnt]['pressure'] = i['pressure']
        weather_data[cnt]['ico'] = i['weather'][0]['icon']

        cnt += 1
    return weather_data


def get_weather_data(lat, lon):
    url = 'https://api.openweathermap.org/data/2.5/onecall'
    query = {
        'appid': API_WEATHER_KEY,
        'lang': 'ru',
        'lat': lat,
        'lon': lon,
        'units': 'metric',
        'exclude': 'current,minutely,hourly,alerts'
    }
    responce = requests.get(url, params=query).json()
    return responce

def get_coord(city):
    """
    Получает координаты по названию города
    """
    query = {'appid': API_WEATHER_KEY,
             'q': city}
    url = 'http://api.openweathermap.org/data/2.5/weather'
    json_data = requests.get(url, params=query).json()

    print(json_data)
    if json_data['cod'] == '404':
        print('Ошибка!')
        # QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Такого города нет')

    lat = json_data['coord']['lat']
    lon = json_data['coord']['lon']
    return lat, lon

def get_ico(weather_data):

    if os.path.exists('icons') == False:
        os.mkdir('icons')

    icons = []
    for j in range(len(weather_data)):
        icons.append(weather_data[j]['ico'])

    for i in icons:
        if os.path.exists(f'icons/{i}.png'):
            continue
        else:
            url_ico = f'http://openweathermap.org/img/wn/{i}@2x.png'
            res = requests.get(url_ico).content
            with (open(f'icons/{i}.png', 'wb')) as f:
                f.write(res)

def main():
    weather_data = pars_weather_data(city)
    get_ico(weather_data)

if __name__ == '__main__':

    main()
