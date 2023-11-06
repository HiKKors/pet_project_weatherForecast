import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from weather_gui import Ui_MainWindow

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


class WeatherForecost(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.api = '96f85f6cff33078c286ea7f114ef1e54'
         
    def get_weather(self):
        try:
            owm = OWM(self.api)
            mgr = owm.weather_manager()


            # Search for current weather in London (Great Britain) and get details
            city_name = self.search_line.text()
            
            observation = mgr.weather_at_place(city_name)
            w = observation.weather
            
            self.city.setText(city_name)
            
            temp = round(w.temperature('celsius')['temp'])
            wet = w.humidity
            sunrise = w.sunrise_time(timeformat='date')
            sunset = w.sunset_time(timeformat='date')
            
            real_sunset = f'{sunset.hours()+4}:{sunset.minutes()}'
            real_sunrise = f'{sunrise.hours()+4}:{sunrise.minutes()}'
            
            self.temperature.setText(f'{str(temp)}°')
            self.wet_text.setText(f'{str(wet)}%')
            self.sunset_text.setText(real_sunset)
            self.sunrise_text.setText(real_sunrise)
        except Exception:
            print('Timeout error')
            
            

        # print(w.detailed_status,     
        #     w.wind(),                 
        #     w.humidity,              
        #     w.temperature('celsius'),  
        #     w.rain,                  
        #     w.heat_index,              
        #     w.clouds)    
        
                   
        
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WeatherForecost()
    form.show()
    app.exec()