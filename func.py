import requests
from datetime import datetime
import locale


locale.setlocale(locale.LC_ALL, "ru")
API_WEATHER_KEY = 'fc3837d82e69a8bea3f8c2a0f1e68643'
city = 'Ростов-на-Дону'

def get_param(city, day=0):
    """
    :return: Кортеж параметров в виде строк
    """
    lat, lon = get_coord(city)
    responce = get_weather_data(lat, lon)
    weather_data = pars_weather_data(responce)

    date = str(weather_data[day]['date'])
    temp = str(weather_data[day]['temp'])
    dow = str(weather_data[day]['dow'])
    descr = str(weather_data[day]['descr'])
    f_l = str(weather_data[day]['f_l'])
    cloudy = str(weather_data[day]['cloudy'])
    preasure = str(weather_data[day]['preasure'])
    ico = str(weather_data[day]['ico'])

    param = (date, temp, dow, descr, f_l, cloudy, preasure, ico)
    return param





def pars_weather_data(responce):
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
        weather_data[cnt]['preasure'] = i['pressure']
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
    lat = requests.get(url, params=query).json()['coord']['lat']
    lon = requests.get(url, params=query).json()['coord']['lon']
    return lat, lon

def main():
    lat, lon = get_coord(city)
    responce = get_weather_data(lat, lon)
    weather_data = pars_weather_data(responce)
    print(get_param(weather_data))

if __name__ == '__main__':

    print(get_param(city))