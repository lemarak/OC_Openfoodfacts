# coding: utf-8

"""
Model User
"""


class User:
    """
    Class User
    """

    def __init__(self, **user):
        self.id_user = user['id_user']
        self.login = user['login']
        self.name = user['name']
        self.password = user['password']

    def __repr__(self):
        str_to_displays = "user: {} ({})"
        return str_to_displays.format(self.login, self.id_user)

    @classmethod
    def get_user(cls, my_db, login):
        """
        Returns a user from his login
        """
        row = my_db.get_rows('users', clause="login = '%s'" % login)
        if row:
            return User(**row[0])
        else:
            return False
