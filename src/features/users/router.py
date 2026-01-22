from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.features.users import services
from .schemas import UserCreate, UserResponse
from src.core.database_connection import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user_endpoint(payload: UserCreate, db: AsyncSession = Depends(get_db)) -> UserResponse:
    try:
        return await services.create_user(db, payload)
    except services.UserAlreadyExists as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
