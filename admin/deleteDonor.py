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
                
                print("\nDonor information deleted successfully.")
            else:
                print("\nDeletion canceled.")
        else:
            print(f"No donor found with ID {donor_id}.")
    except IOError:
        print("Error: Unable to delete donor information. Please try again later.")
