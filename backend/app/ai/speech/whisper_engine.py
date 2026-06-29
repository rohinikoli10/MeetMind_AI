import time
from pathlib import Path
from app.core.config import settings
from faster_whisper import WhisperModel

from app.ai.models.transcription_result import (
    TranscriptionResult,
)


class WhisperEngine:
    """
    Handles speech-to-text transcription
    using Faster-Whisper.
    """

    MODEL_NAME = settings.WHISPER_MODEL

    _model = None

    @classmethod
    def get_model(cls):
        """
        Load the Whisper model only once.
        """
        print("Loading Whisper model...")

        if cls._model is None:

            cls._model = WhisperModel(
                cls.MODEL_NAME,
                device=settings.WHISPER_DEVICE,
                compute_type=settings.WHISPER_COMPUTE_TYPE,
            )
            print("Whisper model loaded successfully.")

        return cls._model

    @classmethod
    def transcribe(
        cls,
        audio_path: str,
    ) -> TranscriptionResult:
        """
        Transcribe audio into text.
        """

        model = cls.get_model()

        start_time = time.time()
        print(f"Starting transcription: {audio_path}")
        segments, info = model.transcribe(
            audio_path,
            beam_size=5,
        )
        print("Transcription finished.")

        transcript = " ".join(
            segment.text.strip()
            for segment in segments
        )

        end_time = time.time()

        return TranscriptionResult(
            text=transcript,
            language=info.language,
            model_name=cls.MODEL_NAME,
            processing_time=round(
                end_time - start_time,
                2,
            ),
            confidence=info.language_probability,
        )