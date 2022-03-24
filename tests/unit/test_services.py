"""
Test ServiceModel
"""
from sqlalchemy import create_engine
from app.models import ServiceModel


def test_can_add_new_service(db):
    model = ServiceModel(db)
    result = model.add(name="service a", price=555.5, os_platform="ios")
    assert result == 1


def test_can_edit_an_existing_service(db):
    model = ServiceModel(db)
    new_id = model.add(name="service a", price=555.5, os_platform="ios")
    assert new_id == 1
    result = model.edit(id=new_id, name="service a", price=555.5, os_platform="ios")
    assert result == 1


def test_can_get_a_service_by_id(db):
    model = ServiceModel(db)
    new_id = model.add(name="service a", price=555.5, os_platform="ios")
    assert new_id == 1

    record = model.get(id=new_id)
    assert record.name == "service a"
    assert float(record.price) == 555.5
    assert record.os_platform == "ios"


def test_can_get_all_services(db):
    model = ServiceModel(db)
    new_id = model.add(name="service a", price=555.5, os_platform="ios")
    new_id2 = model.add(name="service b", price=333.3, os_platform="android")
    assert new_id == 1
    assert new_id2 == 2

    records = model.get_all()
    assert len(records) == 2

    assert records[0].name == "service a"
    assert float(records[0].price) == 555.5
    assert records[0].os_platform == "ios"

    assert records[1].name == "service b"
    assert float(records[1].price) == 333.3
    assert records[1].os_platform == "android"
