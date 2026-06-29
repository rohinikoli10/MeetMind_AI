from sqlalchemy.orm import Session

from app.models.transcript import Transcript


class TranscriptRepository:
    """
    Handles database operations for transcripts.
    """

    @staticmethod
    def create_transcript(
        db: Session,
        transcript: Transcript,
    ) -> Transcript:
        """
        Save a transcript to the database.
        """

        db.add(transcript)
        db.commit()
        db.refresh(transcript)

        return transcript

    @staticmethod
    def get_by_meeting_id(
        db: Session,
        meeting_id: int,
    ) -> Transcript | None:
        """
        Retrieve transcript for a meeting.
        """

        return (
            db.query(Transcript)
            .filter(Transcript.meeting_id == meeting_id)
            .first()
        )



    @staticmethod
    def delete_transcript(
        db: Session,
        transcript: Transcript,
    ) -> None:
        """
        Delete transcript.
        """

        db.delete(transcript)
        db.commit()


 