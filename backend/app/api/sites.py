from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.site import Site
from app.schemas.site import SiteCreate
from uuid import UUID
from app.schemas.site import SiteResponse

router = APIRouter(
    prefix="/sites",
    tags=["Sites"]
)


@router.post(
    "",
    response_model=SiteResponse
)
def create_site(
    site: SiteCreate,
    db: Session = Depends(get_db)
):

    existing = (
        db.query(Site)
        .filter(Site.name == site.name)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Site already exists"
        )

    db_site = Site(
        name=site.name,
        description=site.description
    )

    db.add(db_site)
    db.commit()
    db.refresh(db_site)

    return db_site


@router.get(
    "",
    response_model=list[SiteResponse]
)
def list_sites(
    db: Session = Depends(get_db)
):
    return db.query(Site).all()


@router.get(
    "/{site_id}",
    response_model=SiteResponse
)
def get_site(
    site_id: UUID,
    db: Session = Depends(get_db)
):

    site = (
        db.query(Site)
        .filter(Site.id == site_id)
        .first()
    )

    if not site:
        raise HTTPException(
            status_code=404,
            detail="Site not found"
        )

    return site


@router.delete(
    "/{site_id}"
)
def delete_site(
    site_id: UUID,
    db: Session = Depends(get_db)
):

    site = (
        db.query(Site)
        .filter(Site.id == site_id)
        .first()
    )

    if not site:
        raise HTTPException(
            status_code=404,
            detail="Site not found"
        )

    db.delete(site)
    db.commit()

    return {
        "message": "Site deleted"
    }
