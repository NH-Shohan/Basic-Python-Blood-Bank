from admin.adminDashboard import admin_dashboard
from auth.adminLogin import login_as_admin
from auth.userLogin import user_auth

while True:
    print("\nBlood Bank Menu:")
    print("1. Login as Admin")
    print("2. Login as User")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == '1':
        login_as_admin()
        # admin_dashboard()
    elif choice == '2':
        user_auth()
    elif choice == '3':
        print("Exiting the Blood Bank system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
