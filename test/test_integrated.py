from app.brewsite import app

client = app.test_client()

def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert b"Seneca" in response.data

def test_breweries():
    response = client.get("/breweries")

    assert response.status_code == 200
    assert b"Seneca" in response.data

def test_beer_types():
    response = client.get("/beer_types")

    assert response.status_code == 200
    assert b"Seneca" in response.data

def test_about():
    response = client.get("/about")

    assert response.status_code == 200
    assert b"Seneca" in response.data

