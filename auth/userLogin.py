def register_user():
    username = input("Enter your user username: ")
    password = input("Enter your user password: ")
    
    try:
        with open("database/users.txt", "a") as file:
            file.write(f"{username} | {password}\n")
        print("User registration successful.")
    except IOError:
        print("Error: Unable to register the user. Please try again later.")

def login_user():
    username = input("Enter your user username: ")
    password = input("Enter your user password: ")
    
    try:
        with open("database/users.txt", "r") as file:
            user_data = file.readlines()
        
        for user in user_data:
            user_username, user_password = user.strip().split(" | ")
            if username == user_username and password == user_password:
                print("User login successful.")
                # Perform user tasks here
                return
        
        print("Invalid user credentials. Please try again.")
    except IOError:
        print("Error: Unable to process the login. Please try again later.")

def user_auth():
    while True:
        print("User Login Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Go back")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Going back to the main menu.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
