from fastapi import APIRouter
from sqlalchemy import text

from database.connection import engine

router = APIRouter()


@router.get("/health")
def health():

    try:

        with engine.connect() as connection:

            connection.execute(
                text("SELECT 1")
            )

        return {
            "status": "UP",
            "database": "CONNECTED"
        }

    except Exception as e:

        return {
            "status": "DOWN",
            "database": "DISCONNECTED",
            "error": str(e)
        }