from werkzeug.security import safe_str_cmp



class User(object):
    """
    User class with id, username and password
    """

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id


# Create a user table by name and by id. This is obviously only a temporary solution, in a real case application the user
# information should be saved in a database
users = [
    User(1, 'monkey1', 'abcxyz'),
    User(2, 'monkey2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def get_auth_token(username, password):
    """
    Function called when /auth endpoint is requested.
    Validates the user and returns it. The JTW extension will return an authentication token to the client

    :param username (string): The username of the user
    :param password (string): The password of the user
    :return User: The user object that is found
    """
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    """
    Function called by the JWT library for authenticaton
    """
    user_id = payload['identity']
    return userid_table.get(user_id, None)