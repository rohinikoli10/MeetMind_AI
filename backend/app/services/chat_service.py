from app.ai.rag.rag_engine import RAGEngine


class ChatService:
    """
    Handles chat requests using the RAG engine.
    """

    @staticmethod
    def ask(
        question: str,
        meeting_id: int | None = None,
    ) -> str:

        return RAGEngine.answer_question(
            question=question,
            meeting_id=meeting_id,
        )