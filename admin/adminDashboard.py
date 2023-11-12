from admin.addAdmin import add_admin
from admin.addDonor import add_donor
from admin.deleteDonor import delete_donor
from admin.editDonor import edit_donor
from admin.viewAllTransactions import view_all_transactions
from shared.searchDonor import search_donor_by_blood_type
from shared.sortDonor import sort_donors_by_blood_type
from shared.viewAllDonors import view_all_donors

def print_yellow(text):
    return f"\033[93m{text}\033[0m"

def admin_dashboard():
    while True:
        print("\n\tAdmin Dashboard:\n")
        print("\t1. Add Admin")
        print("\t2. Add Donor")
        print("\t3. View All Donors")
        print("\t4. Search Donor")
        print("\t5. Sort Donors")
        print("\t6. Edit Donor Information")
        print("\t7. Delete Donor Information")
        print("\t8. View All Transactions")
        print("\t9. Logout")
        
        choice = input("\nEnter your choice (1-9): ")
        
        if choice == '1':
            add_admin()
        elif choice == '2':
            add_donor()
        elif choice == '3':
            view_all_donors()
        elif choice == '4':
            search_donor_by_blood_type()
            pass
        elif choice == '5':
            sort_donors_by_blood_type()
            pass
        elif choice == '6':
            edit_donor()
            pass
        elif choice == '7':
            view_all_donors()
            delete_donor()
            pass
        elif choice == '8':
            view_all_transactions()
            pass
        elif choice == '9':
            print("\nLogging out of admin account.")
            break
        else:
            print(print_yellow("\nInvalid choice. Please enter a number from 1 to 9."))
