import json
from json import JSONDecodeError

from functions import add_todo


def get_data():
    try:
        with open('users.json') as f:
            users: list = json.load(f)
            return users
    except (FileNotFoundError, JSONDecodeError):
        with open('users.json', 'w') as f:
            json.dump([], f, indent=4)
            users = []
            return users


def get_todo_data():
    try:
        with open('todos.json') as f:
            todos: list = json.load(f)
            return todos
    except (FileNotFoundError, JSONDecodeError):
        with open('todos.json', 'w') as f:
            json.dump([], f, indent=4)
            todos = []
            return todos


class User:
    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.__password = password

    def append_to_json(self):
        if not self.userExists():
            user = {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'username': self.username,
                'password': self.__password
            }
            users: list = get_data()
            users.append(user)
            with open('users.json', 'w') as f:
                json.dump(users, f, indent=4)
            print('Successfully registered')
        else:
            print('Username or email already exists!')

    def userExists(self):
        users: list = get_data()
        for user in users:
            if user['username'] == self.username or user['email'] == self.email:
                return True
        return False

    def add_todo_for_user(self, text, expires_at):
        add_todo(text, expires_at, self.username)


class Todo:
    def __init__(self, text, expires_at, owner):
        self.text = text
        self.expires_at = expires_at
        self.owner = owner
        self.ID = 0

    def to_dict(self):
        return {
            'ID': self.ID,
            'text': self.text,
            'expires_at': self.expires_at,
            'owner': self.owner
        }


def display_todos(owner):
    todos: list = get_todo_data()
    user_todos = [todo for todo in todos if todo['owner'] == owner]
    print('\nYour Todos:')
    for todo in user_todos:
        print(f"ID: {todo['ID']}, Text: {todo['text']}, Expires At: {todo['expires_at']}")
