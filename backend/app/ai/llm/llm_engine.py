import json

from groq import Groq

from app.core.config import settings


class LLMEngine:
    """
    Unified interface for all LLM providers.
    """

    _client = None

    @classmethod
    def get_client(cls):

        if cls._client is None:

            if settings.LLM_PROVIDER.lower() == "groq":

                cls._client = Groq(
                    api_key=settings.GROQ_API_KEY,
                )

            else:

                raise ValueError(
                    "Unsupported LLM provider."
                )

        return cls._client

    @classmethod
    def generate_json(
        cls,
        prompt: str,
    ) -> dict:

        client = cls.get_client()

        response = client.chat.completions.create(

            model=settings.LLM_MODEL,

            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],

            temperature=0.2,

            response_format={
                "type": "json_object"
            },
        )

        content = response.choices[0].message.content

        return json.loads(content)
    

    @classmethod
    def generate_text(
        cls,
        prompt: str,
    ) -> str:

        client = cls.get_client()

        response = client.chat.completions.create(

        model=settings.LLM_MODEL,

        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],

        temperature=0.2,
        )

        return response.choices[0].message.content