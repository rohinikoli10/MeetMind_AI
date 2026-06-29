from typing import List

from app.ai.models.chunk_result import ChunkResult


class Chunker:
    """
    Splits transcripts into overlapping chunks
    suitable for embedding.
    """

    DEFAULT_CHUNK_SIZE = 500

    DEFAULT_OVERLAP = 100

    @classmethod
    def chunk_text(
        cls,
        transcript: str,
        meeting_id: int,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        overlap: int = DEFAULT_OVERLAP,
    ) -> List[ChunkResult]:

        chunks = []

        start = 0

        chunk_id = 1

        text_length = len(transcript)

        while start < text_length:

            end = min(
                start + chunk_size,
                text_length,
            )

            chunk_text = transcript[start:end].strip()

            if chunk_text:

                chunks.append(

                    ChunkResult(

                        chunk_id=chunk_id,

                        meeting_id=meeting_id,

                        text=chunk_text,

                        metadata={
                            "start": start,
                            "end": end,
                        },
                    )
                )

                chunk_id += 1

            start += chunk_size - overlap

        return chunks