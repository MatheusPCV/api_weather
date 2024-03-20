from datetime import datetime

class WeatherEntity:
    def __init__(self, temperature, date, city='', atmosphericPressure='', humidity='', weather=''):
        self.temperature = temperature
        self.date = date
        self.city = city
        self.atmosphericPressure = atmosphericPressure
        self.humidity = humidity
        self.weather = weather

    def __str__(self):
        return f"Weather <{self.temperature}>"