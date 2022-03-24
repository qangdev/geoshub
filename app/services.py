from app import models


def fetch_service(db, request_url, service_id: int):
    try:
        model = models.ServiceModel(db)
        record = model.get(service_id)
        return {"data": record}
    finally:
        models.ActivityModel(db).add(request_url)


def fetch_services(db, request_url, name: str, price: float, os: str):
    try:
        model = models.ServiceModel(db)
        records = model.get_all(name=name, price=price, os=os)
        return {"count": len(records), "data": records}
    finally:
        if name or price or os:
            models.ActivityModel(db).add(request_url)
