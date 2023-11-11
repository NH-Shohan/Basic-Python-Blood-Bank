def print_red(text):
    return f"\033[91m{text}\033[0m"
def print_blue(text):
    return f"\033[94m{text}\033[0m"

def add_admin():
    try:
        admin_username = input("\nEnter new admin username: ").lower()
        admin_password = input("Enter new admin password: ")

        with open("database/admins.txt", "a") as file:
            file.write(f"{admin_username} | {admin_password}\n")

        print(print_blue("\nAdmin added successfully!"))
    except IOError:
        print(print_red("\nError: Unable to add admin. Please try again later."))
