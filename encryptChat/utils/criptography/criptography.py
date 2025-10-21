from cryptography.fernet import Fernet

class Crypto:
    def __init__(self, key=None):
        """
        Initializes the encryption object.
        If no key is provided, generates a new key.

        :param key: Encryption key (optional)
        """
        # No key passed: gen a new key
        if key is None:
            self.key = Fernet.generate_key()

        # otherwise: use key
        else:
            self.key = key
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, message):
        """
         I Encrypt a message.

        :param message: Message to be encrypted (string or bytes)

        :return: Encrypted message in base64 (bytes)
        """
        # convert message to bytes if it's a string
        if isinstance(message, str):
            message = message.encode('utf-8')

        # encrypt binary
        encrypted_message = self.cipher_suite.encrypt(message)
        return encrypted_message

    def decrypt(self, encrypted_message):
        """
        I decrypt an encrypted message.

        :param encrypted_message: Encrypted message (bytes)

        :return: Decrypted message (bytes)
        """
        # decrypt message
        decrypted_message = self.cipher_suite.decrypt(encrypted_message)
        return decrypted_message

    def get_key(self):
        """
        I return the encryption key.

        :return: Encryption key (bytes)
        """
        # return encryption key
        return self.key
