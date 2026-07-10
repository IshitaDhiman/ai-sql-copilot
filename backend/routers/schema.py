from fastapi import APIRouter

from services.schema_service import fetch_schema

router = APIRouter()


@router.get("/schema")
def get_schema():

    return fetch_schema()