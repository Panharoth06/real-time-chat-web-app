from sqlalchemy.ext.asyncio import AsyncSession
from src.features.users import crud
from src.features.users.models import User
from .schemas import UserCreate, UserResponse

class UserAlreadyExists(Exception):
    pass

class UserNotFound(Exception):
    pass

async def create_user(db: AsyncSession, payload: UserCreate) -> UserResponse:
    existing = await crud.get_user_by_username(db, payload.username)
    if existing:
        raise UserAlreadyExists("User Already Exists")
    
    user: User = await crud.create_user(db, payload.username)
    return UserResponse.model_validate(user)

