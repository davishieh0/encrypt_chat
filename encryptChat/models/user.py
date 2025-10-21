# Imports
from db.mongoClient import getDb

def getUser(fieldName: str, value: str):
    """
    Get one user from database

    :param fieldName: field name to search
    :param value: value to match

    :return: user document or None
    """

    # Get database instance
    db = getDb()

    # Get users collection
    collection = db.get_collection('users')

    # Find and return user by field
    result = collection.find_one({fieldName: value})
    return result

def createUser(data: dict):
    """
    Create a new user in database

    :param data: user data dictionary

    :return: insert result
    """

    # Get database instance
    db = getDb()

    # Get users collection
    collection = db.get_collection('users')

    # Insert new user and return result
    result = collection.insert_one(data)
    return result
