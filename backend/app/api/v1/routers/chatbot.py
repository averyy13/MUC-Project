from fastapi import APIRouter, status

from app.schemas.chatbot import (
    ChatRequest,
    ChatResponse,
)
from app.services.chatbot_service import ChatbotService
from app.services.chatbot_service import ChatbotService


router = APIRouter(
    prefix="/chatbot",
    tags=["Medical Chatbot"],
)


@router.post(
    "/chat",
    response_model=ChatResponse,
    status_code=status.HTTP_200_OK,
)
async def chat_with_medical_copilot(
    request: ChatRequest,
):
    reply = await ChatbotService.chat(
        message=request.message
    )

    return ChatResponse(
        reply=reply
    )