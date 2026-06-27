from sqlalchemy.orm import Session

from app.models.meeting import Meeting
from app.constants.meeting_status import MeetingStatus


class MeetingRepository:

    @staticmethod
    def create_meeting(
        db: Session,
        meeting: Meeting
    ) -> Meeting:
        """
        Save a new meeting to the database.
        """

        db.add(meeting)
        db.commit()
        db.refresh(meeting)

        return meeting

    @staticmethod
    def get_meeting_by_id(
        db: Session,
        meeting_id: int
    ) -> Meeting | None:
        """
        Retrieve a meeting by its ID.
        """

        return (
            db.query(Meeting)
            .filter(Meeting.id == meeting_id)
            .first()
        )

    @staticmethod
    def get_user_meetings(
        db: Session,
        user_id: int
    ):
        """
        Retrieve all meetings uploaded by a user.
        """

        return (
            db.query(Meeting)
            .filter(Meeting.user_id == user_id)
            .order_by(Meeting.created_at.desc())
            .all()
        )

    @staticmethod
    def update_processing_status(
        db: Session,
        meeting: Meeting,
        status: MeetingStatus
    ) -> Meeting:
        """
        Update processing status.
        """

        meeting.processing_status = status

        db.commit()
        db.refresh(meeting)

        return meeting

    @staticmethod
    def update_duration(
        db: Session,
        meeting: Meeting,
        duration: int
    ) -> Meeting:
        """
        Update meeting duration.
        """

        meeting.duration_seconds = duration

        db.commit()
        db.refresh(meeting)

        return meeting

    @staticmethod
    def delete_meeting(
        db: Session,
        meeting: Meeting
    ) -> None:
        """
        Delete a meeting.
        """

        db.delete(meeting)
        db.commit()