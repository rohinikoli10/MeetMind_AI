from fastapi import APIRouter, Depends

from app.core.oauth2 import get_current_user

from app.schemas.chat_schema import (
    ChatRequest,
    ChatResponse,
)

from app.services.chat_service import ChatService


router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"],
)


@router.post(
    "/",
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
    current_user=Depends(get_current_user),
):

    answer = ChatService.ask(
        question=request.question,
    )

    return ChatResponse(
        answer=answer
    )


@router.post(
    "/meeting/{meeting_id}",
    response_model=ChatResponse,
)
def chat_single_meeting(
    meeting_id: int,
    request: ChatRequest,
    current_user=Depends(get_current_user),
):

    answer = ChatService.ask(
        question=request.question,
        meeting_id=meeting_id,
    )

    return ChatResponse(
        answer=answer
    )