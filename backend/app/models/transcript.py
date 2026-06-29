from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    Float,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.database.database import Base


class Transcript(Base):
    __tablename__ = "transcripts"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    meeting_id = Column(
        Integer,
        ForeignKey(
            "meetings.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        unique=True,
        index=True,
    )

    transcript_text = Column(
        Text,
        nullable=False,
    )

    language = Column(
        String(20),
        nullable=False,
        default="unknown",
    )

    model_name = Column(
        String(50),
        nullable=False,
    )

    processing_time = Column(
        Float,
        nullable=True,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    meeting = relationship(
        "Meeting",
        back_populates="transcript",
    )