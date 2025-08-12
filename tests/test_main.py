import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "Present Agent API" in response.json()["message"]


def test_instagram_webhook_verification():
    """Test Instagram webhook verification"""
    # This would fail without proper tokens, but tests the endpoint exists
    response = client.get(
        "/webhook/instagram?hub.mode=subscribe&hub.challenge=test&hub.verify_token=invalid"
    )
    # Expecting 403 because we don't have valid tokens in test
    assert response.status_code == 403