from django.conf import settings
import pymongo

class WeatherRepository:
    collection = ''

    def __init__(self, collectionName) -> None:
        self.collection = collectionName

    def getConnection(self):
        client = pymongo.MongoClient(settings.MONGO_CONNECTION_STRING)
        connection = client[settings.MONGO_DATABASE_NAME]
        return connection
    
    def getCollection(self):  
        conn = self.getConnection()
        collection = conn[self.collection]
        return collection
    
    def getAll(self):
        document = self.getCollection().find({})
        return document
    
    def insert(self, weather_entity):
        serialized_data = {
            "temperature": weather_entity.temperature,
            "date": weather_entity.date,
            "city": weather_entity.city,
            "atmosphericPressure": weather_entity.atmosphericPressure,
            "humidity": weather_entity.humidity,
            "weather": weather_entity.weather
        }
        self.getCollection().insert_one(serialized_data)