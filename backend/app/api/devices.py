from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.dependencies import get_db
from app.models.device import Device
from app.models.site import Site
from app.models.credential import CredentialProfile
from app.schemas.device import DeviceCreate, DeviceResponse

router = APIRouter(prefix="/devices", tags=["Devices"])


@router.post("", response_model=DeviceResponse)
def create_device(device: DeviceCreate, db: Session = Depends(get_db)):
    if not db.query(Site).filter(Site.id == device.site_id).first():
        raise HTTPException(status_code=404, detail="Site not found")

    if not db.query(CredentialProfile).filter(CredentialProfile.id == device.credential_id).first():
        raise HTTPException(status_code=404, detail="Credential not found")

    if db.query(Device).filter(Device.hostname == device.hostname).first():
        raise HTTPException(status_code=409, detail="Device already exists")

    db_device = Device(**device.model_dump())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device


@router.get("", response_model=list[DeviceResponse])
def list_devices(db: Session = Depends(get_db)):
    return db.query(Device).all()


@router.get("/{device_id}", response_model=DeviceResponse)
def get_device(device_id: UUID, db: Session = Depends(get_db)):
    device = db.query(Device).filter(Device.id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device


@router.delete("/{device_id}")
def delete_device(device_id: UUID, db: Session = Depends(get_db)):
    device = db.query(Device).filter(Device.id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    db.delete(device)
    db.commit()
    return {"message": "Device deleted"}
