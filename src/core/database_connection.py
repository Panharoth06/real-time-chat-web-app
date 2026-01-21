from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from src.config.database_config import DATABASE_URL

# Async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Async session factory
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

# Dependency to use in routes
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
