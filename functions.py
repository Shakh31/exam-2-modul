import json
from users import get_data, get_todo_data, User, Todo, display_todos


def register():
    first_name = input('Enter your first_name: ')
    last_name = input('Enter your last_name: ')
    email = input('Enter your email: ')
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    user = User(first_name, last_name, email, username, password)
    user.append_to_json()


def log_in():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    k = 0

    users: list = get_data()
    for user in users:
        if user['username'] == username and user['password'] == password:
            print('Logged in: ')
            display_todos(username)
            break
        else:
            k += 1
    if k == len(users):
        print('Incorrect username or password')


def add_todo(text, expires_at, owner):
    todo = Todo(text, expires_at, owner)
    todos: list = get_todo_data()
    todo_id = len(todos) + 1
    todo_data = todo.to_dict()
    todo_data['ID'] = todo_id
    todos.append(todo_data)
    with open('todos.json', 'w') as f:
        json.dump(todos, f, indent=4)
    print('Todo added successfully')


def remove_todo(todo_id):
    todos: list = get_todo_data()
    updated_todos = [todo for todo in todos if todo['ID'] != todo_id]
    with open('todos.json', 'w') as f:
        json.dump(updated_todos, f, indent=4)
    print('Todo removed successfully')


def update_todo(todo_id, text, expires_at):
    todos: list = get_todo_data()
    updated_todos = []
    for todo in todos:
        if todo['ID'] == todo_id:
            todo['text'] = text
            todo['expires_at'] = str(expires_at)
        updated_todos.append(todo)
    with open('todos.json', 'w') as f:
        json.dump(updated_todos, f, indent=4)
    print('Todo updated successfully')



