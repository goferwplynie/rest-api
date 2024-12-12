import json
from flask import request, jsonify
from flask.typing import ResponseReturnValue


class User_controller:
    @staticmethod
    def get_user(user_id: int = None) -> ResponseReturnValue:
        with open("./app/users.json") as f:
            users = json.load(f)
        if user_id != None:
            for user in users:
                if user["id"] == user_id:
                    return user
            return "", 400
        return users

    @staticmethod
    def add_user(user: dict) -> ResponseReturnValue:
        user_id = None
        with open("./app/users.json") as f:
            users = json.load(f)

        if users:
            for i in range(len(users) - 1):
                if users[i]["id"] + 1 != users[i + 1]["id"]:
                    user_id = users[i]["id"] + 1
                    break

            if user_id == None:
                user_id = users[-1]["id"] + 1
        else:
            user_id = 1

        user["id"] = user_id
        users.append(user)
        users = sorted(users, key=lambda x: x["id"])
        with open("./app/users.json", "w") as f:
            json.dump(users, f)
        return user, 201

    @staticmethod
    def update_user(user_id: int, user: dict) -> ResponseReturnValue:
        with open("./app/users.json") as f:
            users = json.load(f)
        key = list(user.keys())[0]
        for i in range(len(users)):
            if users[i]["id"] == user_id:
                users[i][key] = user[key]
                user = users[i]
                print(user)
                with open("./app/users.json", "w") as f:
                    json.dump(users, f)
                return "", 204
        return "", 400

    @staticmethod
    def put_user(user_id: int, user: dict) -> ResponseReturnValue:
        with open("./app/users.json") as f:
            users = json.load(f)
        for i in range(len(users)):
            if users[i]["id"] == user_id:
                user["id"] = user_id
                users[i] = user
                with open("./app/users.json", "w") as f:
                    json.dump(users, f)
                return "", 204

    @staticmethod
    def delete_user(user_id: int) -> ResponseReturnValue:
        with open("./app/users.json") as f:
            users: list = json.load(f)
        for i in range(len(users)):
            if users[i]["id"] == user_id:
                users.pop(i)
                with open("./app/users.json", "w") as f:
                    json.dump(users, f)
                return "", 204
        return "", 400
