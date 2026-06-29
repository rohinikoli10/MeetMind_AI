from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy.orm import relationship

from app.database.database import Base


class MeetingAnalysis(Base):
    __tablename__ = "meeting_analysis"

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

    summary = Column(
        Text,
        nullable=False,
    )

    minutes_of_meeting = Column(
        Text,
        nullable=False,
    )

    action_items = Column(
        JSONB,
        nullable=False,
    )

    decisions = Column(
        JSONB,
        nullable=False,
    )

    key_topics = Column(
        JSONB,
        nullable=False,
    )

    sentiment = Column(
        String(30),
        nullable=False,
    )

    model_name = Column(
        String(100),
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    meeting = relationship(
        "Meeting",
        back_populates="analysis",
    )