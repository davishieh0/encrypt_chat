# Imports
from utils.constants import URI, DATABASE
from pymongo import MongoClient

class MongoDB:
    """
    MongoDB connection singleton
    """
    _instance = None
    client = None
    db = None

    def __new__(cls):
        """
        Create singleton instance of MongoDB connection

        :return: MongoDB instance
        """

        # Check if instance exists, create if not
        if cls._instance is None:
            # Validate required environment variables
            if not URI:
                raise ValueError("MONGODB_URI environment variable is required")
            if not DATABASE:
                raise ValueError("MONGODB_DATABASE environment variable is required")

            cls._instance = super().__new__(cls)
            cls._instance.client = MongoClient(URI)
            cls._instance.db = cls._instance.client.get_database(DATABASE)

        # Return singleton instance
        return cls._instance

    def getDb(self):
        """
        Get database instance

        :return: Database instance
        """

        # Return database instance
        return self.db

    def close(self):
        """
        Close MongoDB connection
        """

        # Close client if exists
        if self.client:
            self.client.close()

    @classmethod
    def close_if_exists(cls):
        """
        Close MongoDB connection only if instance exists
        """

        # Close connection if instance exists
        if cls._instance is not None and cls._instance.client:
            cls._instance.client.close()

def getDb():
    """
    Get database instance

    :return: Database instance
    """

    # Get MongoDB singleton instance
    mongo = MongoDB()

    # Return database instance
    return mongo.getDb()
