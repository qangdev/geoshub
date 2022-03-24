from fastapi import FastAPI

from app.database import metadata, engine
from app.settings import Settings
from app.routers import activities, services


app = FastAPI()
app.settings = Settings()


@app.on_event("startup")
def onstartup():
    metadata.create_all(engine)


app.include_router(services.router, prefix=app.settings.API_PREFIX)
app.include_router(activities.router, prefix=app.settings.API_PREFIX)
