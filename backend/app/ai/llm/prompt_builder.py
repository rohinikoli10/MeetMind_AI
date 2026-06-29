class PromptBuilder:
    """
    Builds prompts for meeting analysis.
    """

    @staticmethod
    def build_meeting_analysis_prompt(
        transcript: str,
    ) -> str:

        return f"""
You are an expert AI meeting assistant.

Analyze the following meeting transcript and return ONLY valid JSON.

Return the response in exactly this format:

{{
    "summary": "...",
    "minutes_of_meeting": "...",
    "action_items": [
        "..."
    ],
    "decisions": [
        "..."
    ],
    "key_topics": [
        "..."
    ],
    "sentiment": "Positive"
}}

Rules:

1. Do not add explanations.
2. Do not use markdown.
3. Return valid JSON only.
4. Extract all action items.
5. Extract all important decisions.
6. Generate a concise summary.
7. Detect the meeting sentiment.

Meeting Transcript:

{transcript}
"""


    @staticmethod
    def build_rag_prompt(
        question: str,
        context: str,
    ) -> str:

        return f"""
    You are MeetMind AI.

    Answer the user's question ONLY using the meeting context provided below.

    Rules:

    1. If the answer is not present in the context, reply:
    "I could not find that information in the uploaded meetings."

    2. Do not make up facts.

    3. Keep the answer concise.

    Meeting Context:

    {context}

    User Question:

    {question}
    """