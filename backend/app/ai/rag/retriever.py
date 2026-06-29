from typing import List

from app.ai.rag.embedding_engine import EmbeddingEngine
from app.ai.rag.vector_store import VectorStore


class Retriever:
    """
    Performs semantic retrieval from ChromaDB.
    """

    DEFAULT_TOP_K = 5

    @classmethod
    def retrieve(
        cls,
        question: str,
        meeting_id: int | None = None,
        top_k: int = DEFAULT_TOP_K,
    ) -> List[str]:

        # Generate embedding for the user question
        model = EmbeddingEngine.get_model()

        query_embedding = model.encode(
            question,
            normalize_embeddings=True,
        ).tolist()

        collection = VectorStore.get_collection()

        query_kwargs = {
            "query_embeddings": [query_embedding],
            "n_results": top_k,
        }

        # Optional filter for a specific meeting
        if meeting_id is not None:
            query_kwargs["where"] = {
                "meeting_id": meeting_id
            }

        results = collection.query(**query_kwargs)

        documents = results.get("documents", [])

        if not documents:
            return []

        return documents[0]