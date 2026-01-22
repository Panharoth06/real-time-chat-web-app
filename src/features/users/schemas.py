from pydantic import BaseModel, ConfigDict
import uuid

class UserCreate(BaseModel):
    username: str
    
    
class UserResponse(BaseModel):
    id: uuid.UUID
    username: str
    
    model_config = ConfigDict(from_attributes=True)