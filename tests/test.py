import sys
from pathlib import Path

# Add parent directory to path to import main
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_sum():
    """Test the sum endpoint"""
    from fastapi.testclient import TestClient
    from main import app

    with TestClient(app) as client:
        response = client.post("/api/sum", json={"first_number": 10, "second_number": 3})
        assert response.status_code == 200
        data = response.json()
        assert data["sum"] == 13 or data.get("result") == 13

def test_subtract():
    """Test the subtract endpoint"""
    from fastapi.testclient import TestClient
    from main import app

    with TestClient(app) as client:
        response = client.post("/api/subtract", json={"first_number": 10, "second_number": 3})
        assert response.status_code == 200
        data = response.json()
        assert data["difference"] == 7 or data.get("result") == 7
