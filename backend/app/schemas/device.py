from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class DeviceCreate(BaseModel):
    hostname: str
    mgmt_ip: str
    platform: str
    vendor: str = "Cisco"
    site_id: UUID
    credential_id: UUID


class DeviceResponse(BaseModel):
    id: UUID
    hostname: str
    mgmt_ip: str
    platform: str
    vendor: str
    site_id: UUID
    credential_id: UUID
    created_at: datetime

    model_config = {"from_attributes": True}
