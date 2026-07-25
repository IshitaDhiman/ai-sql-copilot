from sentence_transformers import SentenceTransformer
from sqlalchemy import text

from database.connection import SessionLocal

MODEL_NAME = "BAAI/bge-small-en-v1.5"

# Load embedding model once
model = SentenceTransformer(MODEL_NAME)


def retrieve_relevant_chunks(question: str, top_k: int = 20):
    """
    Retrieve the most relevant knowledge chunks using pgvector.
    """

    db = SessionLocal()

    try:

        question_embedding = model.encode(
            question,
            normalize_embeddings=True,
            convert_to_numpy=True
        ).tolist()

        sql = text("""
            SELECT
                document_name,
                section_name,
                content,
                embedding <=> CAST(:embedding AS vector) AS distance
            FROM app.knowledge_chunks
            ORDER BY embedding <=> CAST(:embedding AS vector)
            LIMIT :top_k
        """)

        result = db.execute(
            sql,
            {
                "embedding": question_embedding,
                "top_k": top_k
            }
        )

        chunks = []

        for row in result:

            chunks.append(
                {
                    "document_name": row.document_name,
                    "section_name": row.section_name,
                    "content": row.content,
                    "distance": float(row.distance)
                }
            )

        return chunks

    finally:
        db.close()


if __name__ == "__main__":

    question = input("Enter your question: ")

    chunks = retrieve_relevant_chunks(question)

    print(f"\nRetrieved {len(chunks)} chunks\n")

    for index, chunk in enumerate(chunks, start=1):

        print("=" * 80)
        print(f"Result #{index}")
        print(f"Document : {chunk['document_name']}")
        print(f"Section  : {chunk['section_name']}")
        print(f"Distance : {chunk['distance']:.4f}")
        print()
        print(chunk["content"][:400])
        print()