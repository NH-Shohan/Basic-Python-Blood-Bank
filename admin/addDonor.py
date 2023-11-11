def print_red(text):
    return f"\033[91m{text}\033[0m"
def print_blue(text):
    return f"\033[94m{text}\033[0m"

def add_donor():
    try:
        with open("database/last_donor_id.txt", "r") as id_file:
            last_donor_id = int(id_file.read())
    except:
        last_donor_id = 0

    last_donor_id += 1

    name = input("Enter donor's name: ")
    age = input("Enter donor's age: ")
    blood_group = input("Enter donor's blood group: ")
    contact = input("Enter contact information: ")
    location = input("Enter donor's location: ")

    donor_info = f"ID: {last_donor_id} ➤ Name: {name},  Age: {age},  Blood Group: {blood_group},  Contact: {contact},  Location: {location} \n\n"

    try:
        with open("database/donorInformation.txt", "a") as file:
            file.write(donor_info)
        print(print_blue("\nDonor information added successfully."))

        with open("database/last_donor_id.txt", "w") as id_file:
            id_file.write(str(last_donor_id))
    except IOError:
        print(print_red("\nError: Unable to add donor information. Please try again later."))
