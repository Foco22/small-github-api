from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_sum():
    r = client.post("/api/sum", json={"first_number": 10, "second_number": 3})
    assert r.status_code == 200
    data = r.json()
    assert data["sum"] == 13 or data.get("result") == 13
