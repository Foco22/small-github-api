from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_subtract():
    r = client.post("/api/subtract", json={"first_number": 10, "second_number": 3})
    assert r.status_code == 200
    data = r.json()
    assert data["sum"] == 7 or data.get("result") == 7
