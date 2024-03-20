from datetime import datetime
from django.views import View
from django.shortcuts import render, redirect
from .repositories import WeatherRepository
from .serializers import WeatherSerializer
from .models import WeatherEntity


class WeatherView(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weathers = repository.getAll()
        serialized_weathers = [WeatherSerializer(
            weather).data for weather in weathers]
        return render(request, "home.html", {"weathers": serialized_weathers})


class WeatherGenerate(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weather_data = {
            "temperature": 58,
            "date": datetime.now(),
            "city": "Votorantim",
            "atmosphericPressure": 1113.25,
            "humidity": 70,
            "weather": "Sunny"
        }
        new_weather = WeatherEntity(**weather_data)
        repository.insert(new_weather)
        return redirect('Weather View')