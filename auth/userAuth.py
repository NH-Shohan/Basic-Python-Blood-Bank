from auth.registerUser import register_user
from auth.userLogin import login_user

def print_yellow(text):
    return f"\033[93m{text}\033[0m"

def user_auth():
    while True:
        print("\n\tUser Login Menu:")
        print("\t1. Register")
        print("\t2. Login")
        print("\t3. Go back")
        
        choice = input("\nEnter your choice (1/2/3): ")
        
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("\nGoing back to the main menu.")
            break
        else:
            print(print_yellow("\nInvalid choice. Please enter 1, 2, or 3."))
