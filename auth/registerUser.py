import re

def print_red(text):
    return f"\033[91m{text}\033[0m"
def print_blue(text):
    return f"\033[94m{text}\033[0m"

def is_username_exists(username, user_data):
    for user in user_data:
        if username in user:
            return True
    return False

def is_strong_password(password):
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$', password))

def register_user():
    try:
        with open("database/last_user_id.txt", "r") as id_file:
            last_user_id = int(id_file.read())
    except FileNotFoundError:
        last_user_id = 0

    last_user_id += 1

    username = input("\nEnter your user username: ").lower()
    password = input("Enter your user password: ")

    initial_balance = 1000

    try:
        with open("database/users.txt", "r") as file:
            user_data = file.readlines()

        if is_username_exists(username, user_data):
            print(print_red("\nError: Username already exists. Please choose a different username."))
            return

        if not is_strong_password(password):
            print(print_red("\nError: Password is not strong enough. It should have at least 8 characters, including at least one uppercase letter, one lowercase letter, and one digit."))
            return

        with open("database/users.txt", "a") as file:
            file.write(f"{last_user_id} | {username} | {password} | {initial_balance}\n")
        print(print_blue("\nUser registration successful!"))

        with open("database/last_user_id.txt", "w") as id_file:
            id_file.write(str(last_user_id))
        
    except IOError:
        print(print_red("\nError: Unable to register the user. Please try again later."))
