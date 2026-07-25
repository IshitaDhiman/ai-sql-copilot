import os

from dotenv import load_dotenv

load_dotenv()


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv(
    "OPENROUTER_MODEL",
    "openai/gpt-oss-20b:free"
)


class Config:

    APP_NAME = os.getenv("APP_NAME")

    DEBUG = os.getenv("DEBUG") == "True"
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    OPENROUTER_MODEL = os.getenv(
        "OPENROUTER_MODEL",
        "qwen/qwen3-coder:free"
    )

    DATABASE = {
        "host": os.getenv("DATABASE_HOST"),
        "port": os.getenv("DATABASE_PORT"),
        "database": os.getenv("DATABASE_NAME"),
        "user": os.getenv("DATABASE_USER"),
        "password": os.getenv("DATABASE_PASSWORD"),
    }


config = Config()