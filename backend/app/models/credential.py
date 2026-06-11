from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
import uuid
from datetime import datetime


class CredentialProfile(Base):
    __tablename__ = "credential_profiles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False, unique=True)
    username = Column(String(100), nullable=False)
    password_encrypted = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
