# Imports
from db.mongoClient import getDb
from bson.objectid import ObjectId

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


def getMessages(receiver: str) -> list:
    """
        Fetches all unread messages for a specific recipient.

        :param receiver: username of the recipient ('to' field).
        :return: A list of message documents (dictionaries).
    """
    db = getDb()
    collection = db.get_collection('message')

    # Query: Searches for messages where 'to' is the receiver AND 'status' is 'unread'
    query = {
        "to": receiver,
        "status": "unread"
    }

    # Returns the messages as a list
    messages = list(collection.find(query))
    return messages


def updateMessageStatus(messageIds: list, status: str) -> int:
    """
        Updates the status of a list of messages.

        :param message_ids: A list of message _id's (strings or ObjectId) to be updated.
        :param status: The new status ('read' or 'unread').
        :return: The number of modified documents.
    """
    db = getDb()
    collection = db.get_collection('message')

    # Converts the IDs to ObjectId, required for MongoDB queries
    object_ids = [ObjectId(id) for id in messageIds]

    # Query: Finds all documents where the _id is in the provided list
    query = {
        "_id": {"$in": object_ids}
    }

    # Update: Sets the 'status' field to the new value
    update_op = {
        "$set": {"status": status}
    }

    result = collection.update_many(query, update_op)
    return result.modified_count