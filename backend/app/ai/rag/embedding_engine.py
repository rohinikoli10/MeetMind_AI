from typing import List

from sentence_transformers import SentenceTransformer

from app.ai.models.chunk_result import ChunkResult
from app.core.config import settings


class EmbeddingEngine:
    """
    Generates vector embeddings for transcript chunks.
    """

    _model = None

    @classmethod
    def get_model(cls):

        if cls._model is None:

            cls._model = SentenceTransformer(
                settings.EMBEDDING_MODEL
            )

        return cls._model

    @classmethod
    def generate_embeddings(
        cls,
        chunks: List[ChunkResult],
    ) -> List[list[float]]:

        model = cls.get_model()

        texts = [
            chunk.text
            for chunk in chunks
        ]

        embeddings = model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return embeddings.tolist()