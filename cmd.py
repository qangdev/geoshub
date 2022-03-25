from importlib.metadata import metadata
import random

from sqlalchemy import insert
from app import models
from app.database import engine, metadata


metadata.create_all(engine)

def add_sample_services():
    connection = engine.connect()
    try:
        os_platforms = ["iso", "android", "linux", "macos"]
        prices = [120.5, 90.3, 150, 200.50, 130.5]
        for i in range(0, 5):
            connection.execute(
                insert(models.tbl_services).values(
                    name=f"service #{i}", 
                    price=prices.pop(), 
                    os_platform=random.choice(os_platforms)
                )
            )
    finally:
        connection.close()


def add_sample_activityes():
    connection = engine.connect()
    try:
        activity_requests = [
            "http://127.0.0.1:8000/api/v1/services/?os=ios",
            "http://127.0.0.1:8000/api/v1/services/?os=ios&name=abc",
            "http://127.0.0.1:8000/api/v1/services/?os=windows&price=555",
            "http://127.0.0.1:8000/api/v1/services/?name=security",
            "http://127.0.0.1:8000/api/v1/services/?name=security&os=macos",
        ]
        for i in range(0, 5):
            connection.execute(
                insert(models.tbl_activities).values(
                    request=activity_requests.pop()
                )
            )
    finally:
        connection.close()


if __name__ == "__main__":
    print('Started...')
    add_sample_services()
    add_sample_activityes()
    print('Done')
