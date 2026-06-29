from sqlalchemy.orm import Session

from app.models.analysis import MeetingAnalysis


class AnalysisRepository:
    """
    Handles database operations for meeting analysis.
    """

    @staticmethod
    def create_analysis(
        db: Session,
        analysis: MeetingAnalysis,
    ) -> MeetingAnalysis:

        db.add(analysis)
        db.commit()
        db.refresh(analysis)

        return analysis

    @staticmethod
    def get_by_meeting_id(
        db: Session,
        meeting_id: int,
    ) -> MeetingAnalysis | None:

        return (
            db.query(MeetingAnalysis)
            .filter(
                MeetingAnalysis.meeting_id == meeting_id
            )
            .first()
        )

    @staticmethod
    def delete_analysis(
        db: Session,
        analysis: MeetingAnalysis,
    ) -> None:

        db.delete(analysis)
        db.commit()