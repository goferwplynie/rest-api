import json
from flask import request, jsonify

class User_controller:
    @staticmethod
    def get_user(user_id: int=None) -> dict:
        with open('users.json') as f:
            users = json.load(f)
        if user_id!=None:
            for user in users:
                if user['id'] == user_id:
                    return jsonify(user)
            return jsonify({'message': 'User not found'})
        return users

    @staticmethod
    def add_user(user: dict) -> dict:
        user_id = None
        with open('users.json') as f:
            users = json.load(f)
        
        for i in range(len(users) - 1):
            if users[i]["id"] + 1 != users[i + 1]["id"]:
                user_id = users[i]["id"] + 1
                break
        
        if user_id == None:
            user_id = users[-1]["id"] + 1

        user['id'] = user_id
        users.append(user)
        with open('users.json', 'w') as f:
            json.dump(users, f)
        return jsonify(user)

    @staticmethod
    def update_user(user_id: int, user: dict) -> dict:
        with open('users.json') as f:
            users = json.load(f)
        key = list(user.keys())[0]
        for i in range(len(users)):
            if users[i]['id'] == user_id:
                users[i][key] = user[key]
                with open('users.json', 'w') as f:
                    json.dump(users, f)
                return jsonify(users[i])
        return jsonify({'message': 'User not found'})