def print_red(text):
    return f"\033[91m{text}\033[0m"

def search_donor_by_blood_type():
    print("\tSelect a blood type to search for:")
    print("\t1. A+")
    print("\t2. A-")
    print("\t3. B+")
    print("\t4. B-")
    print("\t5. AB+")
    print("\t6. AB-")
    print("\t7. O+")
    print("\t8. O-")

    blood_type_choices = {
        "1": "A+",
        "2": "A-",
        "3": "B+",
        "4": "B-",
        "5": "AB+",
        "6": "AB-",
        "7": "O+",
        "8": "O-",
    }

    choice = input("\nEnter the number of the blood type you want to search for: ")
    
    selected_blood_type = blood_type_choices.get(choice)
    
    if selected_blood_type is not None:
        try:
            with open("database/donorInformation.txt", "r") as file:
                donors = file.readlines()
            
            found_donors = []
            for donor in donors:
                if f"Blood Group: {selected_blood_type}" in donor:
                    found_donors.append(donor)
            
            if found_donors:
                print("\nDonors with matching blood type:")
                for found_donor in found_donors:
                    print(found_donor)
            else:
                print(f"\nNo {selected_blood_type} donors found.")
        except IOError:
            print(*print_red("\nError: Unable to search for donors. Please try again later."))
    else:
        print(print_red("\nInvalid choice. Please select a valid blood type."))