import json
from src.app import app

def test_health_check():
    client = app.test_client()
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.data.decode() == "pong"

def test_add_numbers_success():
    client = app.test_client()
    response = client.post("/add", json={"a": 3, "b": 4})
    assert response.status_code == 200
    result = response.get_json()
    assert isinstance(result, dict)
    assert result["result"] == 7

def test_add_numbers_invalid_input():
    client = app.test_client()
    response = client.post("/add", json={"x": 1})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
