from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class CredentialCreate(BaseModel):
    name: str
    username: str
    password: str


class CredentialResponse(BaseModel):
    id: UUID
    name: str
    username: str
    created_at: datetime

    model_config = {"from_attributes": True}
