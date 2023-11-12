from user.userDashboard import user_dashboard

def print_red(text):
    return f"\033[91m{text}\033[0m"
def print_blue(text):
    return f"\033[94m{text}\033[0m"
def print_yellow(text):
    return f"\033[93m{text}\033[0m"

def login_user():
    username = input("\nEnter your user username: ").lower()
    password = input("Enter your user password: ")

    try:
        with open("database/users.txt", "r") as file:
            user_data = file.readlines()

        for user in user_data:
            user_info = user.strip().split(" | ")

            if len(user_info) == 4:
                user_id, user_username, user_password, balance = user_info
                if username == user_username and password == user_password:
                    print(print_blue("\nUser login successful!"))
                    user_dashboard(user_id)
                    return

        print(print_yellow("\nInvalid user credentials. Please try again."))
    except IOError:
        print(print_red("\nError: Unable to process the login. Please try again later."))
