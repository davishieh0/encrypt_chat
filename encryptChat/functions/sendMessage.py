from utils.criptography.criptography import Crypto
from models.message import createMessage

def sendMessage(sender: str,
                receiver: str,
                message: str,
                encryption_key: bytes = None
):
    """
    Send an encrypted message

    :param sender: sender username
    :param receiver: receiver username
    :param message: message to be sent
    :param encryption_key: encryption key (optional, generates new if not provided)

    :return: result of message insert operation
    """

    try:
        # Create crypto instance with provided key (or generate new one)
        crypto = Crypto(key=encryption_key)
        encryptedMsg = crypto.encrypt(message)

        # Build message document
        json = {
            'from':sender,
            'to': receiver,
            'message': encryptedMsg,
            'status': 'unread',
        }

        # Insert message into database and return result
        return createMessage(json)

    except Exception as e:
        raise Exception("The following error occurred: ", e)
