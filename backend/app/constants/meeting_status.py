from enum import Enum


class MeetingStatus(str, Enum):
    UPLOADED = "uploaded"
    PROCESSING = "processing"
    TRANSCRIBED = "transcribed"
    SUMMARIZED = "summarized"
    COMPLETED = "completed"
    FAILED = "failed"