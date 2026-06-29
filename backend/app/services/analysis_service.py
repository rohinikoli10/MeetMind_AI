from sqlalchemy.orm import Session

from app.ai.llm.meeting_analyzer import MeetingAnalyzer
from app.models.analysis import MeetingAnalysis
from app.repositories.analysis_repository import AnalysisRepository
from app.repositories.transcript_repository import TranscriptRepository


class AnalysisService:
    """
    Handles AI analysis of meeting transcripts.
    """

    @staticmethod
    def analyze_meeting(
        db: Session,
        meeting_id: int,
    ) -> MeetingAnalysis:

        transcript = TranscriptRepository.get_by_meeting_id(
            db,
            meeting_id,
        )

        if transcript is None:
            raise ValueError("Transcript not found.")

        result = MeetingAnalyzer.analyze(
            transcript.transcript_text
        )

        analysis = MeetingAnalysis(
            meeting_id=meeting_id,
            summary=result.summary,
            minutes_of_meeting=result.minutes_of_meeting,
            action_items=result.action_items,
            decisions=result.decisions,
            key_topics=result.key_topics,
            sentiment=result.sentiment,
            model_name=result.model_name,
        )

        return AnalysisRepository.create_analysis(
            db,
            analysis,
        )