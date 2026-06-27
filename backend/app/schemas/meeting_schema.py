from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from app.constants.meeting_status import MeetingStatus
from app.constants.meeting_type import MeetingType


class MeetingCreate(BaseModel):
    """
    Metadata required to create a meeting.
    File upload is handled separately.
    """

    title: str = Field(..., min_length=3, max_length=255)

    description: Optional[str] = None

    meeting_type: MeetingType


class MeetingResponse(BaseModel):
    """
    Response returned after meeting creation.
    """

    id: int

    title: str

    description: Optional[str]

    meeting_type: MeetingType

    processing_status: MeetingStatus

    duration_seconds: Optional[int]

    original_filename: str

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)