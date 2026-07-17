# Import modules
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read values
api_key = os.getenv("API_KEY")
db_password = os.getenv("DB_PASSWORD")