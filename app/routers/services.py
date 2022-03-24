from typing import Optional

from fastapi import APIRouter, Depends, Request
from sqlalchemy.engine.base import Connection


from app import schema
from app import models
from app import services as app_services
from app.database import get_db


router = APIRouter(prefix="/services", tags=["services"])


@router.post("/")
def post_services(obj: schema.NewService, db: Connection = Depends(get_db)):
    model = models.ServiceModel(db)
    id = model.add(**obj.dict())
    return {"message": "OK", "record": id}


@router.put("/")
def put_services(obj: schema.EditSerive, db: Connection = Depends(get_db)):
    model = models.ServiceModel(db)
    id = model.update(**obj)
    return {"message": "OK", "record": id}


@router.get("/{service_id}")
def get_service(request: Request, service_id: int, db: Connection = Depends(get_db)):
    return app_services.fetch_services(
        db=db, request_url=str(request.url), service_id=service_id
    )


@router.get("/")
def get_services(
    request: Request,
    name: Optional[str] = None,
    price: Optional[float] = None,
    os: Optional[str] = None,
    db: Connection = Depends(get_db),
):
    return app_services.fetch_services(
        db=db, request_url=str(request.url), name=name, price=price, os=os
    )


@router.delete("/")
def delete_services(service_id: int, db: Connection = Depends(get_db)):
    model = models.ServiceModel(db)
    id = model.delete(service_id)
    return {"message": "OK", "record": id}
