def print_red(text):
    return f"\033[91m{text}\033[0m"

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
        print(print_red("\nError: Unable to view donor information. Please try again later."))