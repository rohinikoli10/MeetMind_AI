from typing import List

import chromadb
from chromadb.config import Settings

from app.ai.models.embedding_result import EmbeddingResult
from app.core.config import settings


class VectorStore:
    """
    Handles all interactions with ChromaDB.
    """

    _client = None
    _collection = None

    @classmethod
    def get_collection(cls):

        if cls._collection is None:

            cls._client = chromadb.PersistentClient(
                path=settings.CHROMA_DB_PATH,
                settings=Settings(
                    anonymized_telemetry=False,
                ),
            )

            cls._collection = cls._client.get_or_create_collection(
                name=settings.CHROMA_COLLECTION,
                metadata={
                    "description": "MeetMind transcript embeddings"
                },
            )

        return cls._collection

    @classmethod
    def add_embeddings(
        cls,
        embeddings: List[EmbeddingResult],
    ) -> None:

        collection = cls.get_collection()

        collection.add(
            ids=[
                embedding.id
                for embedding in embeddings
            ],

            embeddings=[
                embedding.vector
                for embedding in embeddings
            ],

            documents=[
                embedding.text
                for embedding in embeddings
            ],

            metadatas=[
                embedding.metadata
                for embedding in embeddings
            ],
        )

    @classmethod
    def delete_meeting(
        cls,
        meeting_id: int,
    ) -> None:

        collection = cls.get_collection()

        collection.delete(
            where={
                "meeting_id": meeting_id
            }
        )

    @classmethod
    def count(cls) -> int:

        return cls.get_collection().count()