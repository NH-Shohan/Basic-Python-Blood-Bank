from admin.adminDashboard import admin_dashboard

def login_as_admin():
    username = input("\nEnter your admin username: ")
    password = input("Enter your admin password: ")
    
    with open("database/admins.txt", "r") as file:
        admin_data = file.readlines()
    
    for admin in admin_data:
        admin_username, admin_password = admin.strip().split(" | ")
        if username == admin_username and password == admin_password:
            print("\nAdmin login successful.")
            admin_dashboard()
            return
    
    print("Invalid admin credentials. Please try again.")