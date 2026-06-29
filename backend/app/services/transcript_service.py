from app.ai.models.transcription_result import TranscriptionResult
from app.ai.speech.audio_pipeline import AudioPipeline
from app.ai.speech.whisper_engine import WhisperEngine
import traceback
from app.constants.meeting_status import MeetingStatus

from app.models.transcript import Transcript
from app.database.database import SessionLocal
from app.repositories.meeting_repository import MeetingRepository
from app.repositories.transcript_repository import TranscriptRepository


class TranscriptService:

    @staticmethod
    def process_meeting(
        meeting_id: int,
    ):

        db = SessionLocal()

        try:

            meeting = MeetingRepository.get_meeting_by_id(
                db,
                meeting_id,
            )

            if meeting is None:
                raise ValueError(
                    "Meeting not found."
                )

            MeetingRepository.update_processing_status(
                db,
                meeting,
                MeetingStatus.PROCESSING,
            )

            wav_file = AudioPipeline.convert_to_wav(
                meeting.recording_path
            )

            result = WhisperEngine.transcribe(
                wav_file
            )

            transcript = Transcript(
                meeting_id=meeting.id,
                transcript_text=result.text,
                language=result.language,
                model_name=result.model_name,
                processing_time=result.processing_time,
            )

            TranscriptRepository.create_transcript(
                db,
                transcript,
            )

            MeetingRepository.update_processing_status(
                db,
                meeting,
                MeetingStatus.COMPLETED,
            )

        except Exception as e:

            print("\n" + "=" * 70)
            print("TRANSCRIPTION ERROR")
            print("=" * 70)

            traceback.print_exc()

            print("=" * 70 + "\n")

            if "meeting" in locals():
                MeetingRepository.update_processing_status(
                db,
                meeting,
                MeetingStatus.FAILED,
                )

            raise

        finally:

            db.close()