import pymongo

class Database(object): # Database class inherits all attributes from object class
    URI = "mongodb://127.0.0.1:27017"  # class attributes which defines a value for every class instance
    DATABASE = None

    @staticmethod
    def initialize():  # method that creates path to desired mongodb database
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['tooldraft']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
