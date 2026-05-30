"""Unit tests for the generated Flask law-firm API."""
import pytest


@pytest.fixture
def client():
    from main import app

    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_health_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json().get("status") == "ok"


def test_list_practice_areas(client):
    response = client.get("/practice-areas")
    assert response.status_code == 200
    data = response.get_json()
    assert "practice_areas" in data
    assert isinstance(data["practice_areas"], list)


def test_post_feedback_creates_entry(client):
    payload = {
        "name": "Test Client",
        "email": "client@example.com",
        "message": "Need consultation about contract review.",
        "type": "inquiry",
    }
    response = client.post("/feedback", json=payload)
    assert response.status_code == 201
    body = response.get_json()
    assert body.get("email") == "client@example.com"

    detail = client.get(f"/feedback/{body['id']}")
    assert detail.status_code == 200
