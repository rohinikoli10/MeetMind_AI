from app.ai.llm.llm_engine import LLMEngine
from app.ai.llm.prompt_builder import PromptBuilder
from app.core.config import settings
from app.ai.models.analysis_result import (
    AnalysisResult,
)


class MeetingAnalyzer:
    """
    Generates AI insights from meeting transcripts.
    """

    @staticmethod
    def analyze(
        transcript: str,
    ) -> AnalysisResult:

        # Step 1
        prompt = (
            PromptBuilder
            .build_meeting_analysis_prompt(
                transcript
            )
        )

        # Step 2
        response = LLMEngine.generate_json(
            prompt
        )

        # Step 3
        return AnalysisResult(

            summary=response.get(
                "summary",
                "",
            ),

            minutes_of_meeting=response.get(
                "minutes_of_meeting",
                "",
            ),

            action_items=response.get(
                "action_items",
                [],
            ),

            decisions=response.get(
                "decisions",
                [],
            ),

            key_topics=response.get(
                "key_topics",
                [],
            ),

            sentiment=response.get(
                "sentiment",
                "Neutral",
            ),

            model_name=settings.LLM_MODEL,
        )