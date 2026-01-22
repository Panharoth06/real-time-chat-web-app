from fastapi import HTTPException, Depends, status, APIRouter
from src.features.chat.rooms.services import RoomNotFound
from src.features.users.services import UserNotFound
from src.features.chat.messages import services
from src.core.database_connection import get_db
from .schemas import MessageCreate, MessageResponse
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

router = APIRouter(prefix='/messages', tags=['Message'])
DBSession = Annotated[AsyncSession, Depends(get_db)]

@router.post('/', response_model=MessageResponse, status_code=status.HTTP_201_CREATED)
async def create_message(message_create: MessageCreate ,db: DBSession):
    try:
        return await services.send_message(db, message_create)
    except RoomNotFound | UserNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get('/{username}', response_model=list[MessageResponse])
async def get_messages_by_user_username(username: str, db: DBSession):
    try: 
        return await services.get_message_by_user_username(db, username)
    except UserNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))