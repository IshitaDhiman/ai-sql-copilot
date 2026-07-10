from pydantic import BaseModel


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    columns: list[str]
    rows: list[list]
    row_count: int
    execution_time_ms: float