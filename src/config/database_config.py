import os
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase

# Load environment variables from .env
load_dotenv()

# Read environment variables
DATABASE_TYPE = os.getenv("DATABASE_TYPE", "postgresql+asyncpg") 
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")
DATABASE_USER = os.getenv("DATABASE_USER", "raidenz")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "qwer")
DATABASE_NAME = os.getenv("DATABASE_NAME", "room_chat_db")

# Construct the async database URL
DATABASE_URL = (
    f"{DATABASE_TYPE}://"
    f"{DATABASE_USER}:{DATABASE_PASSWORD}@"
    f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)

# Shared ORM base for all models
class Base(DeclarativeBase):
    pass
