from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP, text
from pgvector.sqlalchemy import Vector

from database.connection import Base


class KnowledgeChunk(Base):
    __tablename__ = "knowledge_chunks"
    __table_args__ = {"schema": "app"}

    chunk_id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    document_name = Column(
        String(100),
        nullable=False
    )

    section_name = Column(
        String(100)
    )

    content = Column(
        Text,
        nullable=False
    )

    embedding = Column(
        Vector(384),
        nullable=False
    )

    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )