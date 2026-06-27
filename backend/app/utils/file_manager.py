import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import HTTPException, UploadFile, status


class FileManager:

    ALLOWED_EXTENSIONS = {
        ".mp3",
        ".wav",
        ".mp4",
        ".m4a",
    }

    MAX_FILE_SIZE = 500 * 1024 * 1024  # 500 MB

    @staticmethod
    def validate_file(file: UploadFile) -> None:
        """
        Validate uploaded file extension.
        """

        extension = Path(file.filename).suffix.lower()

        if extension not in FileManager.ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=(
                    "Unsupported file format. "
                    "Allowed formats: mp3, wav, mp4, m4a."
                ),
            )

    @staticmethod
    def generate_filename(original_filename: str) -> str:
        """
        Generate a unique filename.
        """

        extension = Path(original_filename).suffix.lower()

        return f"{uuid4()}{extension}"

    @staticmethod
    def create_upload_directory() -> Path:
        """
        Create upload directory if it does not exist.
        """

        upload_path = Path("uploads") / "meetings"

        upload_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        return upload_path

    @staticmethod
    def save_file(
        file: UploadFile,
        filename: str,
    ) -> str:
        """
        Save uploaded file.
        """

        upload_directory = FileManager.create_upload_directory()

        file_path = upload_directory / filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return str(file_path)

    @staticmethod
    def delete_file(file_path: str) -> None:
        """
        Delete file if it exists.
        """

        path = Path(file_path)

        if path.exists():
            path.unlink()