# This file wil the core mongodb management client

def get_database(name):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://AfeefNeo:qwerty123@cluster0.2p5oz.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create or/and get the instence of the database 
    if not name:
        name = 'default'
    return client[name]
