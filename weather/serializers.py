class WeatherSerializer:
    def __init__(self, data, many=False) -> None:
        if many:
            weathers = []
            for weather in data:
                weathers.append(weather)
            self.data = weathers
        else:
            self.data = {
                "temperature": data.temperature,
                "city": data.city,
                "atmosphericPressure": data.atmosphericPressure,
                "humidity": data.humidity,
                "weather": data.weather,
                "date": data.date.strftime("%Y-%m-%d %H:%M:%S"),
            }
