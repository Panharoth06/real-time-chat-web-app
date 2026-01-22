from src.features.chat.rooms import crud
from .models import Room
from .schemas import RoomCreate, RoomResponse
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

class RoomAlreadyExists(Exception):
    pass

class RoomNotFound(Exception):
    pass


async def create_room_chat(db: AsyncSession, payload: RoomCreate) -> RoomResponse:
    is_exists = await crud.get_room_chat_by_name(db, payload.name)
    
    if is_exists:
        raise RoomAlreadyExists("Room already exists, try a different name :)")
    
    room: Room = await crud.create_room_chat(db ,payload.name) 
    return RoomResponse.model_validate(room)       

async def get_room_by_id(db: AsyncSession, room_id: uuid.UUID) -> RoomResponse:
    exists = await crud.get_room_chat_by_id(db, room_id)
    
    if not exists:
        raise RoomNotFound(f"Room with ID: {room_id} is not exists :(")
    
    return RoomResponse.model_validate(exists) 

async def get_room_chat_by_name(db: AsyncSession, room_name: str) -> RoomResponse:
    exists = await crud.get_room_chat_by_name(db, room_name)
    
    if not exists:
        raise RoomNotFound(f"Room with name {room_name} not found :(")
    
    return RoomResponse.model_validate(exists)


async def get_room_model_by_name(
    db: AsyncSession,
    room_name: str
) -> Room | None:
    return await crud.get_room_chat_by_name(db, room_name)