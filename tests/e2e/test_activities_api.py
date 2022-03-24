"""
Test Activity API
"""


def test_get_activites(client):
    response = client.get("/api/v1/activities/")
    assert response.status_code == 200


def test_post_new_activity(client):
    payload = {"name": "http://example.com?p=1"}

    response = client.post("/api/v1/activities/", json=payload)

    assert response.status_code == 200
    assert response.json() == {"message": "OK", "record": 1}
