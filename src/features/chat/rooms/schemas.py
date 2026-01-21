from pydantic import BaseModel
import uuid

class RoomCreate(BaseModel):
    room_name: str

class RoomResponse(BaseModel):
    id: uuid.UUID
    room_name: str
    