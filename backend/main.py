from fastapi import FastAPI

from config import config
from routers.health import router as health_router
from routers.schema import router as schema_router
from routers.query import router as query_router

app = FastAPI(
    title=config.APP_NAME
)

app.include_router(health_router)
app.include_router(schema_router)
app.include_router(query_router)