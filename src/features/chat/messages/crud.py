import uuid
from .schemas import MessageResponse
from sqlalchemy.ext.asyncio import AsyncSession
from src.features.users.models import User
from src.features.chat.rooms.models import Room
from src.features.chat.messages.models import Message

async def create_message(db: AsyncSession, content: str, sender: User, room: Room) -> Message:
    message = Message(content=content, sender_id=sender.id, room_id=room.id)
    db.add(message)
    await db.commit()
    await db.refresh(message)
    
    return message