import pymongo

class Database:
    # If we don't want to create object, we don't have to use __init__ method
    URI = 'mongodb://127.0.0.1:27017'
    DATABASE = None

    @staticmethod #use this to define static method
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['blog_app']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

