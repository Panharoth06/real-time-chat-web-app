from pydantic import BaseModel, Field, ConfigDict
import uuid
from src.features.chat.messages.schemas import MessageResponse


class RoomCreate(BaseModel):
    name: str


class RoomResponse(BaseModel):
    id: uuid.UUID
    name: str
    messages: list[MessageResponse] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)