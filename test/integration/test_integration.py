from app.app import app
from pytest import fixture
from flask.testing import FlaskClient
import json


@fixture
def client() -> FlaskClient:
    return app.test_client()

def reset_file():
    with open("./app/users.json", "w") as f:
        json.dump([], f)

def test_get_all_users(client: FlaskClient):
    with open("./app/users.json", "w") as f:
        json.dump([{"id":1,"name": "Dawid", "lastname": "Markiewicz"}], f)
    response = client.get("users")

    assert response.status_code == 200

def test_get_user_by_id(client: FlaskClient):
    response = client.get("users/1")

    assert response.status_code == 200

def test_get_user_wrong_id(client: FlaskClient):
    response  = client.get("users/38021")

    assert response.status_code == 400

def test_patch_user(client: FlaskClient):
    request_json = {"name":"aaaa"}

    response = client.patch("users/1", json=request_json)

    assert response.status_code == 204

def test_patch_wrong_user(client: FlaskClient):
    request_json = {"name":"aaaa"}

    response = client.patch("users/139821", json=request_json)

    assert response.status_code == 400

def test_put_user(client: FlaskClient):
    request_json = {"name":"Dawid", "lastname": "aaaaa"}

    response = client.put("users/1", json=request_json)

    assert response.status_code == 204

def test_delete_user(client: FlaskClient):
    response = client.delete("users/1")

    assert response.status_code == 204

def test_delete_wrong_user(client: FlaskClient):
    response = client.delete("users/901421")

    assert response.status_code == 400

def post_user(client: FlaskClient):
    request_json = {"name": "Dawid", "lastname": "Markiewicz"}

    response = client.post("/users", json=request_json)