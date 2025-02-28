class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_authenticated = False

    def authenticate(self, password):
        if self.password == password:
            self.is_authenticated = True
            return True
        return False

    def get_user_info(self):
        return {
            "username": self.username,
            "is_authenticated": self.is_authenticated
        }