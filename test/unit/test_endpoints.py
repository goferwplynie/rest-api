from app.app import app
from pytest import fixture
from flask.testing import FlaskClient


@fixture
def client() -> FlaskClient:
    return app.test_client()


def test_get_endpoint_users(client: FlaskClient):
    response = client.get("/users")
    assert response.json == [
        {"name": "Dawid", "lastname": "ababa", "id": 1},
        {"name": "Dawid2", "lastname": "ababa", "id": 2},
    ]
    assert response.status_code == 200


def test_get_endpoint_users_id(client: FlaskClient):
    response = client.get("/users/1")
    assert response.json == {"name": "Dawid", "lastname": "ababa", "id": 1}
    assert response.status_code == 200


def test_get_endpoint_users_wrong_id(client: FlaskClient):
    response = client.get("/users/398012")
    assert response.status_code == 400


def test_post_user_endpoint(client: FlaskClient):
    user = {"name": "Dawid", "lastname": "Markiewicz"}
    wanted_user = {"name": "Dawid", "lastname": "Markiewicz", "id": 3}
    response = client.post("/users", json=user)
    assert response.json == wanted_user
    assert response.status_code == 201
