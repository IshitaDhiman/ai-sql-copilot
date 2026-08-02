from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from config import config
from routers.health import router as health_router
from routers.schema import router as schema_router
from routers.query import router as query_router
from routers.sql import router as sql_router

app = FastAPI(
    title="AI SQL Copilot",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(health_router)
app.include_router(schema_router)
app.include_router(query_router)
app.include_router(sql_router)

@app.get("/")
def home():
    return {
        "message": "AI SQL Copilot Running"
    }