class User:
    def login(self):
        print("Login")
class BusinessUser(User):
    def run_add(self):
        print("Run Add")
b = BusinessUser()
b.login()
b.run_add()