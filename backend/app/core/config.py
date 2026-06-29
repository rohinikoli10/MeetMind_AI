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


settings = Settings()