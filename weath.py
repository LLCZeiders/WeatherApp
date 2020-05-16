from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from weather import Ui_weatherapp
import json
import requests

class weather_window(QtWidgets.QMainWindow, Ui_weatherapp):
    api_key = 'xxx'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    zip_code = '94016'
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.update()

    def update(self):
        complete_url = "{}{}{}{}{}{}".format(self.base_url, 'zip=', self.zip_code, '&units=imperial','&appid=', self.api_key)
        response = requests.get(complete_url)
        x = response.json()
        weather = x['main']
        description = x['weather'][0]['description']

        self.city_name.setText(x['name'])
        self.weather_status.setText(description)

        self.temp_label.setText(self.temp_label.text() + str(weather['temp']) + ' F')
        self.feels_label.setText(self.feels_label.text() + str(weather['feels_like']) + ' F')
        self.humid_label.setText(self.humid_label.text() + str(weather['humidity']) + '%')
        self.pressure_label.setText(self.pressure_label.text() + str(weather['pressure']) + ' HPA')
        self.wind_label.setText(self.wind_label.text() + str(x['wind']['speed']) + ' m/h')

        icon_image = QPixmap("C:/Users/llcze/Desktop/icons/weather/" + x['weather'][0]['icon'] + '.png')

        self.icon.setPixmap(icon_image)
