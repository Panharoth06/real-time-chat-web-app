import uuid
from .schemas import MessageResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select
from src.features.users.models import User
from src.features.chat.rooms.models import Room
from src.features.chat.messages.models import Message

async def create_message(db: AsyncSession, content: str, sender: User, room: Room) -> Message:
    message = Message(content=content, sender_id=sender.id, room_id=room.id)
    db.add(message)
    await db.commit()
    await db.refresh(message)
    
    return message


async def get_message_by_user(db: AsyncSession, ownername: str) -> list[Message]:
    messages = await db.execute(select(Message).options(selectinload(Message.sender)).where(User.username == ownername))
    return messages.scalars().all()