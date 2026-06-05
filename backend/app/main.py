from fastapi import FastAPI

app = FastAPI(
    title="NetOps Center",
    version="0.1.0"
)

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
