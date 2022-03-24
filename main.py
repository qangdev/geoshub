import uvicorn
from app.application import app


if __name__ == "__main__":
    uvicorn.run(
        app=app, host=str(app.settings.APP_HOST), port=int(app.settings.APP_PORT)
    )
