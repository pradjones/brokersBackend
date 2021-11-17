from fastapi import FastAPI
import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from config import settings

from apps.routers.repository import router as repository_router
from apps.routers.jobs import router as jobs_router

app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
    # app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
    # app.mongodb = app.mongodb_client[settings.DB_NAME]
    pass


@app.on_event("shutdown")
async def shutdown_db_client():
    # app.mongodb_client.close()
    pass


app.include_router(repository_router, tags=["Repositories"], prefix="")
app.include_router(jobs_router, tags=["Jobs"], prefix="")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )