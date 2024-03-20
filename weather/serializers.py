class WeatherSerializer:
    def __init__(self, instance):
        self.instance = instance

    @property
    def data(self):
        serialized_data = {
            "temperature": self.instance.get('temperature', None),
            "date": self.instance.get('date', None),
            "city": self.instance.get('city', None),
            "atmosphericPressure": self.instance.get('atmosphericPressure', None),
            "humidity": self.instance.get('humidity', None),
            "weather": self.instance.get('weather', None)
        }
        return serialized_data