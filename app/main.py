from fastapi import FastAPI

from app.core.config import settings
from app.core.database import Base, engine
from app.models import *
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


@app.get("/")
def health_check():
    return {
        "message": "Multi Vendor Inventory System Running"
    }