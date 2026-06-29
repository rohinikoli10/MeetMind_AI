from dataclasses import dataclass
from typing import Optional


@dataclass
class TranscriptionResult:
    """
    Standard transcription result returned by any
    speech-to-text engine.
    """

    text: str

    language: str

    model_name: str

    processing_time: float

    confidence: Optional[float] = None