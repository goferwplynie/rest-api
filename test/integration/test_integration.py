from app.app import app
from pytest import fixture
from flask.testing import FlaskClient


@fixture
def client() -> FlaskClient:
    return app.test_client()
