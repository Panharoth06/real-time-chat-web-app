# src/features/chat/messages/schemas.py

from pydantic import BaseModel, ConfigDict
from datetime import datetime
import uuid
from src.features.users.schemas import UserResponse

class MessageResponse(BaseModel):
    id: uuid.UUID
    content: str
    created_at: datetime
    sender: UserResponse

    model_config = ConfigDict(from_attributes=True)

class MessageCreate(BaseModel):
    content: str
    sender_username: str
    room_name: str