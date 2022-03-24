from fastapi import APIRouter, Depends, Query
from sqlalchemy.engine.base import Connection


from app import schema
from app.database import get_db
from app.models import ActivityModel


router = APIRouter(prefix="/activities", tags=["activities"])


@router.post("/")
def post_activities(obj: schema.Activity, db: Connection = Depends(get_db)):
    model = ActivityModel(db)
    id = model.add(**obj.dict())
    return {"message": "OK", "record": id}


@router.get("/")
def get_activities(db: Connection = Depends(get_db)):
    model = ActivityModel(db)
    records = model.get_all()
    return {"count": len(records), "data": records}
