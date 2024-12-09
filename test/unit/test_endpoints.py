from app.app import app
from pytest import fixture
from flask.testing import FlaskClient
import json


@fixture
def client() -> FlaskClient:
    return app.test_client()


def test_get_endpoint_users(client: FlaskClient):
    response = client.get("/users")
    with open("./app/users.json") as f:
        users = json.load(f)
    assert response.json == users
    assert response.status_code == 200


def test_get_endpoint_users_id(client: FlaskClient):
    response = client.get("/users/1")
    assert response.status_code == 200


def test_get_endpoint_users_wrong_id(client: FlaskClient):
    response = client.get("/users/398012")
    assert response.status_code == 400


