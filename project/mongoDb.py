from dotenv import dotenv_values
from mongoengine import connect


config = dotenv_values(".env")
connect(host=config["ATLAS_URI"])

# This file wil the core mongodb management client

def get_database(name):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = config["ATLAS_URI"]

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create or/and get the instence of the database 
    if not name:
        name = 'default'
    return client[name]
