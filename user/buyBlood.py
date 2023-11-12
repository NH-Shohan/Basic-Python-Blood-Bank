prices = {
        'A+': 100,
        'A-': 250,
        'B+': 100,
        'B-': 200,
        'AB+': 100,
        'AB-': 250,
        'O+': 100,
        'O-': 250,
    }

def print_red(text):
    return f"\033[91m{text}\033[0m"
def print_blue(text):
    return f"\033[94m{text}\033[0m"
def print_yellow(text):
    return f"\033[93m{text}\033[0m"

def calculate_blood_price(blood_group, bags_needed):
    total_price = prices.get(blood_group, 0) * bags_needed
    return total_price

def validate_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print(print_red("Invalid input. Please try again."))

def is_valid_age(age):
    return age.isdigit() and 0 < int(age) < 150

def is_valid_blood_group(blood_group):
    return blood_group.upper() in prices

def is_valid_bags_needed(bags_needed):
    return bags_needed.isdigit() and int(bags_needed) > 0

def buy_blood(user_id):
    try:
        with open("database/users.txt", "r") as file:
            user_data = file.readlines()

        for i, user in enumerate(user_data):
            user_info = user.strip().split(" | ")
            existing_user_id, user_balance = user_info[0], user_info[-1]

            if existing_user_id.isdigit() and user_balance.isdigit():
                existing_user_id = int(existing_user_id)
                user_balance = int(user_balance)

                if int(user_id) == existing_user_id:
                    break
        else:
            print(print_red("\nError: Unable to find user information. Purchase canceled."))
            return

    except IOError:
        print(print_red("\nError: Unable to access user balance. Purchase canceled."))
        return

    patient_name = validate_input("\nEnter patient's name: ", lambda x: x.isalpha())
    age = validate_input("Enter patient's age: ", is_valid_age)
    blood_group = validate_input("Enter patient's blood group: ", is_valid_blood_group).upper()
    bags_needed = validate_input("Enter the number of bags needed: ", is_valid_bags_needed)
    location = validate_input("Enter patient's location: ", lambda x: bool(x))

    total_price = calculate_blood_price(blood_group, int(bags_needed))
    
    print(f"\n\t+---------------------------------------------+")
    print(f"\t|  Your Current Balance is:            ${user_balance}  |")
    print(f"\t|---------------------------------------------|")
    if blood_group == 'AB+' or blood_group == 'AB-':
        print(f"\t|  Per Bag {blood_group} blood is:               ${prices.get(blood_group, 0)}   |")
    else:
        print(f"\t|  Per Bag {blood_group} blood is:                ${prices.get(blood_group, 0)}   |")
    print(f"\t|---------------------------------------------|")
    print(f"\t|  Total Blood Price:                  ${total_price}   |")
    print(f"\t|---------------------------------------------|")
    print(f"\t|  Your balance Will be:               ${user_balance - total_price}   |")
    print(f"\t+---------------------------------------------+")


    confirm = input("\nDo you want to proceed with the purchase? (y/n): ").lower()

    try:
        with open("database/users.txt", "r") as file:
            user_data = file.readlines()

        for i, user in enumerate(user_data):
            existing_user_id, _, _, existing_user_balance = user.strip().split(" | ")
            if int(user_id) == int(existing_user_id):
                existing_user_balance = int(existing_user_balance)
                break
        else:
            print(print_red("\nError: Unable to find user information. Purchase canceled."))
            return

    except IOError:
        print(print_red("\nError: Unable to access user balance. Purchase canceled."))
        return

    if confirm == 'y':
        if total_price > existing_user_balance:
            print(print_yellow("\nInsufficient balance. Purchase canceled."))
        else:
            existing_user_balance -= total_price

            try:
                with open("database/users.txt", "r") as file:
                    user_data = file.readlines()

                with open("database/users.txt", "w") as file:
                    for user in user_data:
                        current_user_id, current_user_username, current_user_password, current_user_balance = user.strip().split(" | ")
                        if int(user_id) == int(current_user_id):
                            file.write(f"{current_user_id} | {current_user_username} | {current_user_password} | {existing_user_balance}\n")
                        else:
                            file.write(user)
            except IOError:
                print(print_red("\nError: Unable to update user balance. Purchase canceled."))
                return

            transaction_info = f"➤ User ID: {user_id}, Patient Name: {patient_name}, Age: {age}, Blood Group: {blood_group}, Bags Needed: {bags_needed}, Location: {location}, Total Price: ${total_price}\n"

            try:
                with open("database/bloodBuy.txt", "a") as file:
                    file.write(transaction_info)

                print(print_blue("\nBlood purchase successful!"))
            except IOError:
                print(print_red("\nError: Unable to record the transaction. Please try again later."))

    else:
        print(print_yellow("\nPurchase canceled!"))