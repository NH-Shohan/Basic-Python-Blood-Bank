def print_red(text):
    return f"\033[91m{text}\033[0m"
def print_yellow(text):
    return f"\033[93m{text}\033[0m"

def sort_donors_by_blood_type():
    try:
        with open("database/donorInformation.txt", "r") as file:
            donors = file.readlines()
        
        if donors:
            sorted_donors = sorted(donors, key=lambda donor: donor.split("Blood Group: ")[-1])
            
            print("\nDonors sorted by blood type:")
            for sorted_donor in sorted_donors:
                print(sorted_donor)
        else:
            print(print_yellow("\nNo donors found in the database."))
    except IOError:
        print(print_red("\nError: Unable to sort donors. Please try again later."))