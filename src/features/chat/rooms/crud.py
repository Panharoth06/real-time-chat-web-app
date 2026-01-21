import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import Room


async def get_room_chat_by_id(db: AsyncSession, room_id: uuid.UUID) -> Room | None:
    room = await db.execute(select(Room).where(Room.id == room_id))
    return room.scalar_one_or_none()


async def get_room_chat_by_name(db: AsyncSession, room_name: str) -> Room | None:
    room = await db.execute(select(room).where(Room.name == room_name))
    return room.scalar_one_or_none()


async def create_room_chat(db: AsyncSession, room_name: str) -> Room:
    room = Room(name=room_name)
    db.add(room)
    db.commit()
    db.refresh(room)
    
    return room
        
