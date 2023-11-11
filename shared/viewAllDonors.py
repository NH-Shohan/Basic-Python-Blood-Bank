def view_all_donors():
    try:
        with open("database/donorInformation.txt", "r") as file:
            donors = file.readlines()
        
        if donors:
            print("\nList of All Donors:")
            for donor in donors:
                print(donor)
        else:
            print("\nNo donor information available.")
    except IOError:
        print("Error: Unable to view donor information. Please try again later.")