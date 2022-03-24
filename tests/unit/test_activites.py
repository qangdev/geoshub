"""
Test ActivityModel
"""
from app.models import ActivityModel


def test_can_add_new_activity(db):
    model = ActivityModel(db)
    result = model.add("http://example.com/page?p=1")
    assert result == 1


def test_can_get_all_activity(db):
    model = ActivityModel(db)
    pages = [
        "http://example.com/page?p=1",
        "http://example.com/page?p=2",
        "http://example.com/page?p=3",
    ]
    for page in pages:
        model.add(page)

    records = model.get_all()
    assert len(records) == 3
