from app.ai.rag.chunker import Chunker
from app.ai.rag.embedding_engine import EmbeddingEngine
from app.ai.rag.vector_store import VectorStore

from app.repositories.transcript_repository import (
    TranscriptRepository,
)

from app.ai.models.embedding_result import (
    EmbeddingResult,
)


class IndexingService:
    """
    Converts meeting transcripts into searchable
    vector embeddings.
    """

    @staticmethod
    def index_meeting(
        db,
        meeting_id: int,
    ) -> None:

        transcript = (
            TranscriptRepository.get_by_meeting_id(
                db,
                meeting_id,
            )
        )

        if transcript is None:
            raise ValueError(
                "Transcript not found."
            )

        # Step 1
        chunks = Chunker.chunk_text(
            transcript=transcript.transcript_text,
            meeting_id=meeting_id,
        )

        # Step 2
        vectors = (
            EmbeddingEngine.generate_embeddings(
                chunks
            )
        )

        # Step 3
        embedding_results = []

        for chunk, vector in zip(chunks, vectors):

            embedding_results.append(

                EmbeddingResult(

                    id=f"{meeting_id}_{chunk.chunk_id}",

                    meeting_id=meeting_id,

                    chunk_id=chunk.chunk_id,

                    text=chunk.text,

                    vector=vector,

                    metadata={
                        "meeting_id": meeting_id,
                        "chunk_id": chunk.chunk_id,
                    },
                )
            )

        # Step 4
        VectorStore.add_embeddings(
            embedding_results
        )
        print("Indexed vectors:", VectorStore.count())