from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

MAX_FILE_SIZE=int(os.getenv("MAX_FILE_SIZE"))

