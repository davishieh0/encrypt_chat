from utils.criptography.criptography import Crypto
from models.message import getMessages
from models.message import updateMessageStatus

def receiveMessage(receiver: str, decryptKey : str , mark_as_read: bool = True) -> list:
    """
        Receives unread messages for a user, decrypts them,
        and optionally marks them as read.

        :param receiver: username of the user receiving the messages.
        :param decryptKey: the decryption key.
        :param mark_as_read: (optional) Whether to mark messages as "read" in the database. Default: True.
        :return: A list of dictionaries containing the decrypted messages.
    """
    try:
        # Initialize the Crypto object with the same key used for encryption
        crypto = Crypto(key=decryptKey)

        # Fetch unread messages
        unread_messages = getMessages(receiver)
        received_messages = []
        messageIdsToUpdate = []

        for msgDoc in unread_messages:
            encryptedMsg = msgDoc['message']

            # Decrypt the message
            # Fernet.decrypt returns bytes, so we decode it to a string
            try:
                decryptedMsgBytes = crypto.decrypt(encryptedMsg)
                decryptedMsg = decryptedMsgBytes.decode('utf-8')

                # Format the message to be easy to handle in main
                received_messages.append({
                    'sender': msgDoc['from'],
                    'message': decryptedMsg,
                    'timestamp': msgDoc.get('timestamp')
                })

                # Store the message ID for status update
                # It's important to ensure this value can be converted to ObjectId
                messageIdsToUpdate.append(msgDoc['_id'])
            except Exception as e:
                print(f"this message dont use this key")

        # Mark messages as read in the database
        if mark_as_read and messageIdsToUpdate:
            updateMessageStatus(messageIdsToUpdate, 'read')

        return received_messages

    except Exception as e:
        # Catch and raise the error, useful for debugging
        raise Exception(f"Failed to receive/decrypt messages for {receiver}. Error: {e}")
