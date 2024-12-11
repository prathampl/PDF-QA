from pydantic import BaseModel

class UserSchema(BaseModel):
    """Pydantic schema for a User."""
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
