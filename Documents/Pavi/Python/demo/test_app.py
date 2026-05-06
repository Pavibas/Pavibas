from app import get_data

def test_get_data():
    data=get_data
    assert "id" in data
    assert data["id"]==1
