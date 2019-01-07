from user import User

users = [User(1, 'Jose', 'mypassword'),
         User(2, 'Mimi', 'secret')]

username_table = {u.username: u for u in users}
userid_table = {u.id:u for u in users}

def authenticate(username, password):
    users = username_table.get(username)

