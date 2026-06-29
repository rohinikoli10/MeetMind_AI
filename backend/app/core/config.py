from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()


class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
    )

    # Whisper Configuration
    WHISPER_MODEL = os.getenv("WHISPER_MODEL", "base")

    WHISPER_DEVICE = os.getenv("WHISPER_DEVICE", "cpu")

    WHISPER_COMPUTE_TYPE = os.getenv(
        "WHISPER_COMPUTE_TYPE",
        "int8"
    )

    # LLM Configuration

    LLM_PROVIDER = os.getenv(
        "LLM_PROVIDER",
        "groq",
    )

    GROQ_API_KEY = os.getenv(
        "GROQ_API_KEY",
    )

    LLM_MODEL = os.getenv(
        "LLM_MODEL",
        "llama-3.3-70b-versatile",
    )


settings = Settings()