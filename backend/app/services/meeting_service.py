from fastapi import UploadFile
from sqlalchemy.orm import Session
from fastapi import HTTPException, UploadFile, status
from app.constants.meeting_status import MeetingStatus
from app.models.meeting import Meeting
from app.repositories.meeting_repository import MeetingRepository
from app.schemas.meeting_schema import MeetingCreate
from app.utils.file_manager import FileManager


class MeetingService:

    @staticmethod
    def upload_meeting(
        db: Session,
        meeting_data: MeetingCreate,
        file: UploadFile,
        current_user,
    ) -> Meeting:

        FileManager.validate_file(file)

        unique_filename = FileManager.generate_filename(
            file.filename
        )

        file_path = FileManager.save_file(
            file,
            unique_filename
        )

        try:

            meeting = Meeting(
                user_id=current_user.id,
                title=meeting_data.title,
                description=meeting_data.description,
                meeting_type=meeting_data.meeting_type,
                recording_path=file_path,
                original_filename=file.filename,
                processing_status=MeetingStatus.UPLOADED,
            )

            return MeetingRepository.create_meeting(
                db,
                meeting
            )

        except Exception:

            FileManager.delete_file(file_path)

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to upload meeting."
            )