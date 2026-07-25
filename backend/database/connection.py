from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import config

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{config.DATABASE['user']}:"
    f"{config.DATABASE['password']}@"
    f"{config.DATABASE['host']}:"
    f"{config.DATABASE['port']}/"
    f"{config.DATABASE['database']}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "options": "-csearch_path=banking,public"
    }
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()