import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    APP_NAME = os.getenv("APP_NAME")

    DEBUG = os.getenv("DEBUG") == "True"

    DATABASE = {
        "host": os.getenv("DATABASE_HOST"),
        "port": os.getenv("DATABASE_PORT"),
        "database": os.getenv("DATABASE_NAME"),
        "user": os.getenv("DATABASE_USER"),
        "password": os.getenv("DATABASE_PASSWORD"),
    }


config = Config()