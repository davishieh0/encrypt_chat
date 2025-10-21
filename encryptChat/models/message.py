# Imports
from db.mongoClient import getDb

def createMessage(data: dict):
    """
    Create a new message in database

    :param data: message data dictionary

    :return: insert result
    """

    # Get database instance
    db = getDb()

    # Get message collection
    collection = db.get_collection('message')

    # Insert new message and return result
    result = collection.insert_one(data)
    return result
