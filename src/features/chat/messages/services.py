from src.features.chat.messages import crud
from src.features.chat.rooms.models import Room
from src.features.users.models import User
from src.features.users.services import get_user_model_by_username
from src.features.chat.rooms.services import get_room_model_by_name
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import MessageResponse, MessageCreate

async def send_message(db: AsyncSession, payload: MessageCreate) -> MessageResponse: 
    user = await get_user_model_by_username(db, payload.sender_username)
    room = await get_room_model_by_name(db, payload.room_name)
    
    message = await crud.create_message(db, payload.content, user, room)
    
    return MessageResponse.model_validate(message)    