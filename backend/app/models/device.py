from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base
import uuid
from datetime import datetime


class Device(Base):
    __tablename__ = "devices"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    hostname = Column(String(100), nullable=False, unique=True)
    mgmt_ip = Column(String(45), nullable=False, unique=True)
    platform = Column(String(50), nullable=False)
    vendor = Column(String(50), nullable=False, default="Cisco")
    site_id = Column(UUID(as_uuid=True), ForeignKey("sites.id"), nullable=False)
    credential_id = Column(UUID(as_uuid=True), ForeignKey("credential_profiles.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    site = relationship("Site", backref="devices")
    credential = relationship("CredentialProfile", backref="devices")
