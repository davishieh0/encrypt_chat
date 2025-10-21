# Imports
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

URI = os.getenv('MONGODB_URI')
DATABASE = os.getenv('MONGODB_DATABASE')
