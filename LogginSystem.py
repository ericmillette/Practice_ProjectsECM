#program asks for username, password, and can create an account to be stored for future use.

class account:
    def __init__(self, user, password):
        self.user = user
        self.password = password

def new_account():
    new_user = account("","")
    new_user.user = input("create username: ")
    new_user.password = input("create password: ")
    return new_user

def login():
    current_user = new_account()
    counter = 1
    while counter <= 3:
        prompt_username = input("Enter your username: ")
        prompt_password = input("Enter your password: ")
        if prompt_username == current_user.user and prompt_password == current_user.password:
            print("Hello Mr. " + (current_user.user).capitalize() + " UwU")
            exit()
        elif prompt_username != current_user.user or prompt_password != current_user.password:
            if counter == 3:
                failed_login = input("you have exceeded the amount of tries. would you like to make a new account (y/n)? ")
                if failed_login == 'y':
                    login()
                else:
                    print("goodbye")
                    exit()
            print("Incorrect username or password. Please try again")
            counter += 1
login()