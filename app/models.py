from datetime import datetime
from sqlalchemy import insert, update, select, delete
from sqlalchemy import (
    Table,
    Column,
    String,
    DateTime,
    Numeric,
    Integer,
    Text,
)

from app.database import metadata


tbl_services = Table(
    "services",
    metadata,
    Column("id", Integer(), primary_key=True),
    Column("name", String(255)),
    Column("price", Numeric()),
    Column("os_platform", String(50)),
)

tbl_activities = Table(
    "activities",
    metadata,
    Column("id", Integer(), primary_key=True),
    Column("request", Text()),
    Column("ts", DateTime(), default=datetime.utcnow),
)


class ServiceModel:
    def __init__(self, db):
        self.db = db

    def add(self, name: str, price: float, os_platform: str):
        ins = insert(tbl_services).values(
            name=name, price=price, os_platform=os_platform
        )
        result = self.db.execute(ins)
        return result.inserted_primary_key[0]

    def edit(self, id: int, name: str, price: float, os_platform: str):
        upt = (
            update(tbl_services)
            .where(tbl_services.c.id == id)
            .values(name=name, price=price, os_platform=os_platform)
        )
        self.db.execute(upt)
        return id

    def get(self, id: int):
        sel = select(tbl_services).where(tbl_services.c.id == id)
        rp = self.db.execute(sel)
        return rp.first()

    def get_all(self, name: str = None, price: float = None, os: str = None):
        sel = select(tbl_services)
        if name:
            sel = sel.where(tbl_services.c.name == name)
        if price:
            sel = sel.where(tbl_services.c.price == price)
        if os:
            sel = sel.where(tbl_services.c.os_platform == os)
        rp = self.db.execute(sel)
        return rp.all()

    def delete(self, id: int):
        dele = delete(tbl_services).where(tbl_services.c.id == id)
        result = self.db.execute(dele)
        return result.deleted_id


class ActivityModel:
    def __init__(self, db):
        self.db = db

    def add(self, request: str):
        ins = insert(tbl_activities).values(request=request)
        result = self.db.execute(ins)
        return result.inserted_primary_key[0]

    def get_all(self):
        sel = select(tbl_activities).order_by(tbl_activities.c.ts)
        rp = self.db.execute(sel)
        return rp.all()
