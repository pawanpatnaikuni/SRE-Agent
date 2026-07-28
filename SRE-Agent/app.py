from fastapi import FastAPI
from webhook import router

app = FastAPI(title="SRE-Agent")

app.include_router(router)


@app.get("/")
def health_check():
    return {
        "status": "running",
        "application": "SRE-Agent"
    }