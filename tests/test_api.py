from fastapi.testclient import TestClient

from app.main import app
from app.meetings import MEETINGS

client = TestClient(app)


def test_get_meeting_returns_200():
    response = client.get("/api/meeting")
    assert response.status_code == 200


def test_get_meeting_returns_valid_meeting_name():
    response = client.get("/api/meeting")
    data = response.json()
    assert "meeting_name" in data
    assert data["meeting_name"] in MEETINGS


def test_get_meeting_returns_different_names():
    names = set()
    for _ in range(5):
        response = client.get("/api/meeting")
        if response.status_code == 200:
            names.add(response.json()["meeting_name"])
    assert len(names) >= 1


def test_rate_limit_returns_429():
    # Exhaust rate limit
    for _ in range(6):
        response = client.get("/api/meeting")
    assert response.status_code == 429
    assert "cut off" in response.json()["error"]
