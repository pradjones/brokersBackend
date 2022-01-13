from fastapi import FastAPI
import uvicorn
from config import settings

from apps.routers.repository import router as repository_router
from apps.routers.jobs import router as jobs_router
from apps.routers.users import router as users_router
from apps.routers.sales import router as sales_router
from apps.routers.suggestions import router as suggestions_router
from apps.routers.policies import router as policies_router
from apps.routers.agents import router as agents_router
from apps.routers.clients import router as clients_router
from apps.routers.auth import router as auth_router

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

app.include_router(repository_router, tags=["Repositories"], prefix=settings.API_VERSION)
app.include_router(jobs_router, tags=["Jobs"], prefix=settings.API_VERSION)
app.include_router(users_router, tags=["Users"], prefix=settings.API_VERSION)
app.include_router(sales_router, tags=["Sales"], prefix=settings.API_VERSION)
app.include_router(suggestions_router, tags=["Suggestions"], prefix=settings.API_VERSION)
app.include_router(policies_router, tags=["Policies"], prefix=settings.API_VERSION)
app.include_router(agents_router, tags=["Agents"], prefix=settings.API_VERSION)
app.include_router(clients_router, tags=["Clients"], prefix=settings.API_VERSION)
app.include_router(auth_router, tags=["Auth"], prefix=settings.API_VERSION)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )