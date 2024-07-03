from dotenv import load_dotenv
import os

load_dotenv()

MONGO_USER = os.environ["MONGO_USER"]
MONGO_PASSWORD = os.environ["MONGO_PASSWORD"]
MONGO_DATABASE = os.environ["MONGO_DATABASE"]
MONGO_SERVER = os.environ["MONGO_SERVER"]
