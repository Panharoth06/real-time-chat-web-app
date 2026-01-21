from fastapi import APIRouter, HTTPException, status, Depends

from src.core.database_connection import get_db
from src.features.chat.rooms import services
from sqlalchemy.ext.asyncio import AsyncSession
from src.features.chat.rooms.schemas import RoomCreate, RoomResponse

router = APIRouter(prefix="/rooms", tags=['Rooms'])

@router.post('/', response_model=RoomResponse, status_code=status.HTTP_201_CREATED)
async def create_room_endpoint(request_body: RoomCreate, db: AsyncSession = Depends(get_db)) -> RoomResponse:
    try:
        await services.create_room_chat(db, request_body)
    except services.RoomAlreadyExists as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
