from datetime import datetime
from random import randrange
from django.views import View
from django.shortcuts import render, redirect
from .models import WeatherEntity
from .repositories import WeatherRepository
from .serializers import WeatherSerializer


class WeatherView(View):
    def get(self, request):
        repository = WeatherRepository(collection_name="weathers")
        weathers = repository.getAll()
        serializer = WeatherSerializer(weathers, many=True)
        return render(request, "home.html", {"weathers": serializer.data})


class WeatherGenerate(View):
    def get(self, request):
        repository = WeatherRepository(collection_name="weathers")
        weather = WeatherEntity(
            temperature=randrange(start=17, stop=40),
            date=datetime.now(),
            city="Tatuí",
            humidity=str(randrange(start=0, stop=100)) + "%",
        )
        serializer = WeatherSerializer(data=weather)
        repository.insert(serializer.data)

        return redirect("Weather View")
