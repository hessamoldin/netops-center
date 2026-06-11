from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class SiteCreate(BaseModel):
    name: str
    description: str | None = None


class SiteResponse(BaseModel):
    id: UUID
    name: str
    description: str | None
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
