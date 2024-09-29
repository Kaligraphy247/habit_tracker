# Database functions

import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine


# Load environment variables
load_dotenv()

# Constants
DEBUG = os.getenv("DEBUG")
DEBUG = True if DEBUG == "True" else False
DATABASE_URL = os.getenv("DATABASE_URL")

if (DATABASE_URL is None) or (DATABASE_URL == ""):
    raise ValueError("DATABASE_URL is not set")

url = f"sqlite:///{DATABASE_URL}"
engine = create_engine(url, echo=DEBUG)

def create_db_and_tables():
    """Create database and tables."""
    SQLModel.metadata.create_all(engine)