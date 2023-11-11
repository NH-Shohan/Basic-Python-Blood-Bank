from admin.adminDashboard import admin_dashboard

def print_red(text):
    return f"\033[91m{text}\033[0m"
def print_blue(text):
    return f"\033[94m{text}\033[0m"

def login_as_admin():
    username = input("\nEnter your admin username: ")
    password = input("Enter your admin password: ")
    
    with open("database/admins.txt", "r") as file:
        admin_data = file.readlines()
    
    for admin in admin_data:
        admin_username, admin_password = admin.strip().split(" | ")
        if username == admin_username and password == admin_password:
            print(print_blue("\nAdmin login successful!"))
            admin_dashboard()
            return
    
    print(print_red("\nInvalid admin credentials. Please try again."))