from fastapi import APIRouter, HTTPException

from schemas.query_schema import (
    QueryRequest,
    QueryResponse,
)

from services.query_service import execute_query

router = APIRouter()


@router.post(
    "/execute-sql",
    response_model=QueryResponse
)
def execute_sql(request: QueryRequest):

    try:

        return execute_query(
            request.query
        )

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )