from django.conf import settings
import pymongo


class WeatherRepository:
    def __init__(self, collection_name) -> None:
        self.collection = collection_name

    def getConnection(self):
        client = pymongo.MongoClient(getattr(settings, "MONGO_CONNECTION_STRING"))
        connection = client[getattr(settings, "MONGO_DATABASE_NAME")]
        return connection

    def getCollection(self):
        conn = self.getConnection()
        collection = conn[self.collection]
        return collection

    def getByAttribute(self, attribute, value):
        document = self.getCollection().find_one({f"{attribute}": value})

    def delete(self, document) -> None:
        self.getCollection().delete_one(document)

    def deleteAll(self) -> None:
        self.getCollection().delete_many({})

    def findOneById(self, id):
        document = self.getCollection().find_one({"_id": id})
        return document

    def getAll(self):
        document = self.getCollection().find({})
        return document

    def insert(self, document):
        document = self.getCollection().insert_one(document)
        return document
