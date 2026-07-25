from sentence_transformers import SentenceTransformer

from database.connection import SessionLocal
from app.models.knowledge_chunk import KnowledgeChunk
from app.rag.chunk_documents import chunk_knowledge_base


MODEL_NAME = "BAAI/bge-small-en-v1.5"


def load_embedding_model():
    """
    Loads the embedding model.
    """

    print("\nLoading embedding model...")

    model = SentenceTransformer(MODEL_NAME)

    print("Embedding model loaded.\n")

    return model


def generate_and_store_embeddings():
    """
    Generates embeddings for all knowledge base chunks
    and stores them in PostgreSQL.
    """

    model = load_embedding_model()

    chunks = chunk_knowledge_base()

    print(f"Total chunks found: {len(chunks)}")

    db = SessionLocal()

    try:

        print("\nClearing existing knowledge chunks...")

        db.query(KnowledgeChunk).delete()

        db.commit()

        print("Existing chunks deleted.\n")

        print("Generating embeddings...\n")

        for index, chunk in enumerate(chunks, start=1):

            embedding = model.encode(
            chunk["content"],
            normalize_embeddings=True,
            convert_to_numpy=True
            ).tolist()

            knowledge_chunk = KnowledgeChunk(
                document_name=chunk["document_name"],
                section_name=chunk["section_name"],
                content=chunk["content"],
                embedding=embedding
            )

            db.add(knowledge_chunk)

            if index % 25 == 0:
                print(f"Processed {index}/{len(chunks)} chunks...")

        db.commit()

        print("\n========================================")
        print("Embedding generation completed.")
        print(f"Inserted {len(chunks)} knowledge chunks.")
        print("========================================\n")

    except Exception as e:

        db.rollback()

        print("\nError occurred while generating embeddings.\n")

        raise e

    finally:

        db.close()


if __name__ == "__main__":

    generate_and_store_embeddings()