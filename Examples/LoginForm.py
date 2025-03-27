class LoginForm:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def confirmation(self):
        print(f"\nWelcome, {self.username}!")

class RegisterForm(LoginForm):
    def __init__(self, username, password, email):
        super().__init__(username, password)
        self.email = email24


new_user = LoginForm(username: 'admin', password: 'password')
new_user.confirmation()

