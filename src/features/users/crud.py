import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.features.users.models import User

async def create_user(db: AsyncSession, username: str) -> User:
    user = User(username=username)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_all_users(db: AsyncSession) -> list[User]:
    result = await db.execute(select(User))
    return result.scalars().all()

async def get_user_by_username(db: AsyncSession, username: str) -> User | None:
    result = await db.execute(select(User).where(User.username == username))
    return result.scalar_one_or_none()

async def get_user_by_id(db: AsyncSession, user_id: uuid.UUID) -> User | None:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()

async def delete_user(db: AsyncSession, user: User) -> None:
    await db.delete(user)
    await db.commit()
