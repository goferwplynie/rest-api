from pytest import fixture
from app.controller import User_controller
import json


@fixture
def controller() -> User_controller:
    return User_controller()


def reset_file():
    with open("./app/users.json", "w") as f:
        json.dump([], f)


def test_get_all_users(controller: User_controller):
    users = controller.get_user()

    assert users == [{"id": 1, "name": "Dawid", "lastname": "Markiewicz"}]


def test_get_user(controller: User_controller):
    users = controller.get_user(1)

    assert users == {"id": 1, "name": "Dawid", "lastname": "Markiewicz"}
    reset_file()


def test_get_user_wrong_id(controller: User_controller):
    users = controller.get_user(999)

    assert users == ("", 400)
    reset_file()


def test_add_user(controller: User_controller):

    wanted_user = {"id": 1, "name": "Dawid", "lastname": "Markiewicz"}
    user = {"name": "Dawid", "lastname": "Markiewicz"}

    controller.add_user(user)

    with open("./app/users.json", "r") as f:
        users = json.load(f)

    assert users[0] == wanted_user
    reset_file()


def test_update_user(controller: User_controller):
    user = {"name": "Dawid", "lastname": "Markiewicz"}

    controller.add_user(user)

    controller.update_user(1, {"name": "Wojciech"})

    with open("./app/users.json", "r") as f:
        users = json.load(f)

    assert users[0] == {"id": 1, "name": "Wojciech", "lastname": "Markiewicz"}
    reset_file()
