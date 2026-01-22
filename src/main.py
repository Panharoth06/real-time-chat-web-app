from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.config.database_config import Base
from src.core.database_connection import engine

# Import all models so SQLAlchemy registers them
#  models
from src.features.users import models as user_models
from src.features.chat.rooms import models as room_models
from src.features.chat.messages import models as message_models

# routers 
from src.features.users.router import router as user_router
from src.features.chat.messages.router import router as message_router
from src.features.chat.rooms.router import router as room_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables...")
    # Async-safe table creation
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(
    title="Real-Time Chat API",
    lifespan=lifespan
)

app.include_router(user_router)
app.include_router(message_router)
app.include_router(room_router)


@app.get("/")
async def home():
    return {"message": "Welcome to FastAPI Real-Time Chat!"}
