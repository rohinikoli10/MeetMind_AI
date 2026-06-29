from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    UploadFile,
    BackgroundTasks,
    status,
)
from sqlalchemy.orm import Session

from app.constants.meeting_type import MeetingType
from app.core.oauth2 import get_current_user
from app.database.database import get_db
from app.schemas.meeting_schema import (
    MeetingCreate,
    MeetingResponse,
)
from app.services.meeting_service import MeetingService


router = APIRouter(
    prefix="/meetings",
    tags=["Meetings"],
)


@router.post(
    "/upload",
    response_model=MeetingResponse,
    status_code=status.HTTP_201_CREATED,
)
def upload_meeting(
    background_tasks: BackgroundTasks,
    title: str = Form(...),
    description: str | None = Form(None),
    meeting_type: MeetingType = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Upload a meeting recording.
    """

    meeting_data = MeetingCreate(
        title=title,
        description=description,
        meeting_type=meeting_type,
    )

    return MeetingService.upload_meeting(
        db=db,
        meeting_data=meeting_data,
        file=file,
        current_user=current_user,
        background_tasks=background_tasks,
    )