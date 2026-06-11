from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.db.dependencies import get_db
from app.models.credential import CredentialProfile
from app.schemas.credential import CredentialCreate, CredentialResponse
from app.core.security import encrypt, decrypt

router = APIRouter(prefix="/credentials", tags=["Credentials"])


@router.post("", response_model=CredentialResponse)
def create_credential(
    credential: CredentialCreate,
    db: Session = Depends(get_db)
):
    existing = db.query(CredentialProfile).filter(
        CredentialProfile.name == credential.name
    ).first()

    if existing:
        raise HTTPException(status_code=409, detail="Credential already exists")

    db_credential = CredentialProfile(
        name=credential.name,
        username=credential.username,
        password_encrypted=encrypt(credential.password)
    )

    db.add(db_credential)
    db.commit()
    db.refresh(db_credential)

    return db_credential


@router.get("", response_model=list[CredentialResponse])
def list_credentials(db: Session = Depends(get_db)):
    return db.query(CredentialProfile).all()


@router.get("/{credential_id}", response_model=CredentialResponse)
def get_credential(credential_id: UUID, db: Session = Depends(get_db)):
    credential = db.query(CredentialProfile).filter(
        CredentialProfile.id == credential_id
    ).first()

    if not credential:
        raise HTTPException(status_code=404, detail="Credential not found")

    return credential


@router.delete("/{credential_id}")
def delete_credential(credential_id: UUID, db: Session = Depends(get_db)):
    credential = db.query(CredentialProfile).filter(
        CredentialProfile.id == credential_id
    ).first()

    if not credential:
        raise HTTPException(status_code=404, detail="Credential not found")

    db.delete(credential)
    db.commit()

    return {"message": "Credential deleted"}
