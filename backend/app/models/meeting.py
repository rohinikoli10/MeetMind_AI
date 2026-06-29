from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    Enum as SQLEnum,
)
from sqlalchemy.orm import relationship

from app.database.database import Base
from app.constants.meeting_type import MeetingType
from app.constants.meeting_status import MeetingStatus


class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    title = Column(
        String(255),
        nullable=False,
    )

    description = Column(
        Text,
        nullable=True,
    )

    meeting_type = Column(
        SQLEnum(MeetingType),
        nullable=False,
    )

    recording_path = Column(
        String(1000),
        nullable=False,
    )

    original_filename = Column(
        String(255),
        nullable=False,
    )

    duration_seconds = Column(
        Integer,
        nullable=True,
    )

    processing_status = Column(
        SQLEnum(MeetingStatus),
        default=MeetingStatus.UPLOADED,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    owner = relationship(
        "User",
        back_populates="meetings",
    )

    transcript = relationship(
        "Transcript",
        back_populates="meeting",
        uselist=False,
        cascade="all, delete-orphan",
    )