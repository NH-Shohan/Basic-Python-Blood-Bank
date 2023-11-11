from admin.addDonor import add_donor
from admin.deleteDonor import delete_donor
from admin.editDonor import edit_donor
from shared.searchDonor import search_donor_by_blood_type
from shared.sortDonor import sort_donors_by_blood_type
from shared.viewAllDonors import view_all_donors

def admin_dashboard():
    while True:
        print("\nAdmin Dashboard:\n")
        print("1. Add Donor")
        print("2. View All Donors")
        print("3. Search Donor")
        print("4. Sort Donors")
        print("5. Edit Donor Information")
        print("6. Delete Donor Information")
        print("7. View All Transactions")
        print("8. Logout")
        
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == '1':
            add_donor()
        elif choice == '2':
            view_all_donors();
        elif choice == '3':
            search_donor_by_blood_type()
            pass
        elif choice == '4':
            sort_donors_by_blood_type()
            pass
        elif choice == '5':
            edit_donor()
            pass
        elif choice == '6':
            view_all_donors();
            delete_donor()
            pass
        elif choice == '7':
            # Implement 'View All Transactions' functionality here
            pass
        elif choice == '8':
            print("Logging out of admin account.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")