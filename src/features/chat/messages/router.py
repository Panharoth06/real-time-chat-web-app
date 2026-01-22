from fastapi import HTTPException, Depends, status, APIRouter
from src.features.chat.rooms.services import RoomNotFound
from src.features.users.services import UserNotFound
from src.features.chat.messages import services
from src.core.database_connection import get_db
from .schemas import MessageCreate, MessageResponse
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix='/messages', tags=['Message'])

@router.post('/', response_model=MessageResponse, status_code=status.HTTP_201_CREATED)
async def create_message(message_create: MessageCreate ,db: AsyncSession = Depends(get_db)):
    try:
        message = await services.send_message(db, message_create)
        return MessageResponse.model_validate(message)
    except RoomNotFound | UserNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
        
