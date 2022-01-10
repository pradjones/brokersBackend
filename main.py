from fastapi import FastAPI
import uvicorn
from config import settings

from apps.routers.repository import router as repository_router
from apps.routers.jobs import router as jobs_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_db_client():
    pass


@app.on_event("shutdown")
async def shutdown_db_client():
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