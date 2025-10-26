from auth import login
from auth import register
from cryptography.fernet import Fernet
from functions.sendMessage import sendMessage
from functions.receiveMensage import receiveMessage
from db.mongoClient import MongoDB

import sys
import atexit

# Register cleanup function to close MongoDB on exit
atexit.register(MongoDB.close_if_exists)

def main():
    """
    Main application entry point
    """

    # Validate command line arguments
    if len(sys.argv) != 2:
       print("Usage: python3 main.py <command>")
       print("Available commands: /send, /register, /recive")
       return

    # Handle /send command
    if sys.argv[1] == '/send':
       # Get credentials from user
       username: str = input('Username: ')
       password: str = input('Password: ')

       # Authenticate user
       print("Authenticating...")
       logged = login(username, password)

       # Login successful: send message
       if logged:
           print("Login successful!")

           # Get message details
           message: str = input('Type your message: ')
           receiver: str = input('Username to send message: ')

           # Ask if user has encryption key
           has_key = input('Do you have an encryption key? (yes/no): ').lower().strip()

           # declaring encryption key variable
           encryption_key: str = None
           # user has key: encode key
           if has_key in ['yes', 'y']:
               # User has a key, ask for it
               keyStr = input('Enter your encryption key: ').strip()
               encryption_key = keyStr.encode()
           else:
               # Generate new key and show to user
               encryption_key = Fernet.generate_key()
               print("\n" + "="*60)
               print("🔑 NEW ENCRYPTION KEY GENERATED")
               print("="*60)
               print(f"Key: {encryption_key.decode()}")
               print("\n⚠️  SAVE THIS KEY! You'll need it to decrypt messages.")
               print("="*60 + "\n")

           # Encrypt and send message
           print("Encrypting and sending message...")
           sendMessage(username, receiver, message, encryption_key)
           print("Message sent successfully!")

       # Login failed
       else:
           print("Login failed!")

    # Handle /register command
    elif sys.argv[1] == '/register':
       # Get credentials from user
       username: str = input('Username: ')
       password: str = input('Password: ')

       # Create new user
       print("Creating user...")
       register(username, password)
       print("User registered successfully!")

    elif sys.argv[1] == '/receive':

        # Get credentials from user
        username: str = input('Username: ')
        password: str = input('Password: ')

        # Authenticate user
        print("Authenticating...")
        logged = login(username, password)
        # If login successful: receive message
        if logged:

            print("Login successful!")

            # Receive and display messages

            decryptKey: str = input('Enter your encryption key: ').strip()

            print("Receiving and decrypting messages...")

            messages = receiveMessage(username, decryptKey)

            if messages:

                print(f"You have received {len(messages)} new message(s):")

                for msg in messages:
                    print(f"--- FROM: {msg['sender']} ---")

                    print(f"MESSAGE: {msg['message']}")

            else:

                print("No new messages.")

    # Unknown command
    else:
        print(f"Unknown command: {sys.argv[1]}")
        print("Available commands: /send, /register, /receive")


if __name__ == "__main__":
    try:
        main()

    except ValueError as e:
        print(f"Error: {e}")
        print("Don't have an account? Type: python3 main.py /register")
        sys.exit(1)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
