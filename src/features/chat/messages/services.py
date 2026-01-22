from src.features.chat.messages import crud
from src.features.chat.rooms.models import Room
from src.features.users.models import User
from src.features.users.services import UserNotFound
from src.features.users.services import get_user_model_by_username
from src.features.chat.rooms.services import get_room_model_by_name
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import MessageResponse, MessageCreate
from pydantic import TypeAdapter

async def send_message(db: AsyncSession, payload: MessageCreate) -> MessageResponse: 
    user = await get_user_model_by_username(db, payload.sender_username)
    room = await get_room_model_by_name(db, payload.room_name)
    message = await crud.create_message(db, payload.content, user, room)
    return MessageResponse.model_validate(message)    


async def get_message_by_user_username(db: AsyncSession, username: str) -> list[MessageResponse]:
    user = await get_user_model_by_username(db, username)
    messages = await crud.get_message_by_user(db, username)
    
    # return [MessageResponse.model_validate(messages) for message in messages]
    return TypeAdapter(list[MessageResponse]).validate_python(messages) # use this method: faster for large lists
    