from src.features.chat.rooms import crud
from .schemas import RoomCreate, RoomResponse
from sqlalchemy.ext.asyncio import AsyncSession

class RoomAlreadyExists(Exception):
    pass

class RoomNotFound(Exception):
    pass


def create_room_chat(db: AsyncSession, payload: RoomCreate) -> RoomResponse:
    is_exists = await crud.get_room_chat_by_name(RoomCreate.room_name)
    
    if is_exists:
        raise RoomAlreadyExists("Room already exists, try a different name :)")
    
    room: Room = await crud.create_room_chat(db ,is_exists.name) 
    return RoomResponse.model_validate(room)       
