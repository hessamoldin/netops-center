from fastapi import FastAPI

from app.api.sites import router as sites_router
from app.api.credentials import router as credentials_router


app = FastAPI(
    title="NetOps Center",
    version="0.1.0"
)


app.include_router(sites_router)
app.include_router(credentials_router)


@app.get("/")
def root():
    return {
        "application": "NetOps Center",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    } 
