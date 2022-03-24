"""
Test Activity API
"""


def test_get_services(client):
    response = client.get("/api/v1/services/")
    assert response.status_code == 200


def test_post_new_services(client):
    payload = {"name": "service a", "price": 555.5, "os_platform": "ios"}

    response = client.post("/api/v1/services/", json=payload)

    assert response.status_code == 200
    assert response.json() == {"message": "OK", "record": 1}


def test_edit_existing_services(client):
    payload = {"name": "service a", "price": 555.5, "os_platform": "ios"}

    response = client.post("/api/v1/services/", json=payload)

    assert response.status_code == 200
    assert response.json() == {"message": "OK", "record": 1}

    update_payload = {
        "id": response.json()["record"],
        "name": "service b",
        "price": 666.6,
        "os_platform": "android",
    }

    response_2 = client.post("/api/v1/services/", json=update_payload)

    assert response_2.status_code == 200
    assert response_2.json() == {"message": "OK", "record": 1}
