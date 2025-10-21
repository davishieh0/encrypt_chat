# Imports
from models.user import getUser, createUser
import bcrypt

def login(username: str, password: str):
    """
    Check if user credentials are valid

    :param username: username
    :param password: password

    :return: True if valid, raises ValueError otherwise
    """

    # Get user from database
    data = getUser('username', username)

    # User not found: raise error
    if data is None:
        raise ValueError("Username or password not found")

    # Check password hash and return result
    checked = bcrypt.checkpw(password.encode(), data['password'])
    return checked

def register(username: str, password: str):
    """
    Register a new user

    :param username: username
    :param password: password

    :return: result of insert operation
    """

    # get user
    existingUser = getUser('username', username)

    # user exists: raise an Exception
    if existingUser:
        raise Exception("User already exists")

    # Hash password with bcrypt
    hashedPassword = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # Insert user into database
    result = createUser({
        'username': username,
        'password': hashedPassword
    })

    # return result of insert operation
    return result
