from functions.sendMessage import sendMessage
from auth import login, register
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
       print("Available commands: /send, /register")
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

           # Encrypt and send message
           print("Encrypting and sending message...")
           sendMessage(username, receiver, message)
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

    # Unknown command
    else:
        print(f"Unknown command: {sys.argv[1]}")
        print("Available commands: /send, /register")


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
