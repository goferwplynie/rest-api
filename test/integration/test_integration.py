from app.app import app
from pytest import fixture
from flask.testing import FlaskClient

@fixture
def client() -> FlaskClient:
    return app.test_client()

def test_create_and_get_user_and_delete_user(client:FlaskClient):
    response = client.post("/users",json={"name":"Dawid", "lastname":"Markiewicz"})
    assert response.status_code == 201
    user_id = response.json["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json == {"name":"Dawid", "lastname":"Markiewicz", "id":user_id}

    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 204

def test_create_user_and_patch_user_and_put_user(client:FlaskClient):
    response = client.post("/users",json={"name":"Dawid", "lastname":"Markiewicz"})
    assert response.status_code == 201
    user_id = response.json["id"]

    response = client.patch(f"/users/{user_id}", json={"name":"David"})
    assert response.status_code == 204

    response = client.put(f"/users/{user_id}", json={"name":"Wojciech", "lastname":"Oczkowski"} )
    assert response.status_code == 204
    