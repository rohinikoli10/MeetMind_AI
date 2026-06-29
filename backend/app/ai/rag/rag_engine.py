from app.ai.llm.llm_engine import LLMEngine
from app.ai.llm.prompt_builder import PromptBuilder
from app.ai.rag.retriever import Retriever


class RAGEngine:
    """
    Handles Retrieval-Augmented Generation.
    """

    @classmethod
    def answer_question(
        cls,
        question: str,
        meeting_id: int | None = None,
    ) -> str:

        # Step 1
        chunks = Retriever.retrieve(
            question=question,
            meeting_id=meeting_id,
        )

        if not chunks:

            return (
                "I could not find any relevant "
                "meeting information."
            )

        # Step 2

        context = "\n\n".join(chunks)

        # Step 3

        prompt = (
            PromptBuilder
            .build_rag_prompt(
                question,
                context,
            )
        )

        # Step 4

        response = LLMEngine.generate_text(
            prompt
        )

        return response