def print_red(text):
    return f"\033[91m{text}\033[0m"
def print_blue(text):
    return f"\033[94m{text}\033[0m"
def print_yellow(text):
    return f"\033[93m{text}\033[0m"

def edit_donor():
    donor_id = input("Enter the ID of the donor you want to edit: ")
    
    try:
        with open("database/donorInformation.txt", "r") as file:
            donors = file.readlines()
        
        found_donor = None
        for i, donor in enumerate(donors):
            if f"ID: {donor_id} " in donor:
                found_donor = donor
                break
        
        if found_donor:
            donor_info = found_donor.split("ID: ")[-1].strip()
            old_name = donor_info.split("Name: ")[-1].split(",")[0]
            old_age = donor_info.split("Age: ")[-1].split(",")[0]
            old_blood_group = donor_info.split("Blood Group: ")[-1].split(",")[0]
            old_contact = donor_info.split("Contact: ")[-1].split(",")[0]
            old_location = donor_info.split("Location: ")[-1].strip()
            
            print("\nCurrent donor information:")
            print(found_donor)
            
            print("\nEnter the new information (or leave empty to keep the current data)")
            
            new_name = input("Enter the new name: ") or old_name
            new_age = input("Enter the new age: ") or old_age
            new_blood_group = input("Enter the new blood group: ") or old_blood_group
            new_contact = input("Enter the new contact information: ") or old_contact
            new_location = input("Enter the new location: ") or old_location
            
            updated_donor = found_donor.replace(f"Name: {old_name},", f"Name: {new_name},").replace(f"Age: {old_age},", f"Age: {new_age},").replace(f"Blood Group: {old_blood_group},", f"Blood Group: {new_blood_group},").replace(f"Contact: {old_contact},", f"Contact: {new_contact},").replace(f"Location: {old_location}", f"Location: {new_location}")
            
            donors[i] = updated_donor
            
            with open("database/donorInformation.txt", "w") as file:
                file.writelines(donors)
            
            print(print_blue("\nDonor information updated successfully."))
        else:
            print(print_yellow(f"\nNo donor found with ID {donor_id}."))
    except IOError:
        print(print_red("\nError: Unable to edit donor information. Please try again later."))