def print_red(text):
    return f"\033[91m{text}\033[0m"
def print_blue(text):
    return f"\033[94m{text}\033[0m"

def delete_donor():
    donor_id = input("Enter the ID of the donor you want to delete: ")
    
    try:
        with open("database/donorInformation.txt", "r") as file:
            donors = file.readlines()
        
        found_donor = None
        for i, donor in enumerate(donors):
            if f"ID: {donor_id} " in donor:
                found_donor = donor
                break
        
        if found_donor:
            print("\nDeleting the following donor:")
            print(found_donor)
            
            confirmation = input("\nAre you sure you want to delete this donor? (y/n): ")
            if confirmation.lower() == "y":
                del donors[i]
            
                with open("database/donorInformation.txt", "w") as file:
                    file.writelines(donors)
                
                print(print_blue("\nDonor information deleted successfully."))
            else:
                print("\nDeletion canceled.")
        else:
            print(print_red(f"\nNo donor found with ID {donor_id}."))
    except IOError:
        print(print_red("\nError: Unable to delete donor information. Please try again later."))
