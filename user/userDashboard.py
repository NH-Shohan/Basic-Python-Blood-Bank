from shared.searchDonor import search_donor_by_blood_type
from shared.sortDonor import sort_donors_by_blood_type
from shared.viewAllDonors import view_all_donors
from user.buyBlood import buy_blood
from user.exportTransaction import export_transaction

def user_dashboard(user_id):
    while True:
        with open("database/users.txt", "r") as file:
            user_data = file.readlines()

        user_balance = 0

        for user in user_data:
            user_info = user.strip().split(" | ")

            if int(user_id) == int(user_info[0]):
                user_balance = int(user_info[-1])
                break
        
        print(f"\n\tUser Dashboard\n\tCurrent Balance: ${user_balance}\n")
        print("\t1. View All the Donor")
        print("\t2. Search Donor")
        print("\t3. Sort Donor")
        print("\t4. Buy Blood")
        print("\t5. Export Transaction")
        print("\t6. Logout")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            view_all_donors()
        elif choice == '2':
            search_donor_by_blood_type()
        elif choice == '3':
            sort_donors_by_blood_type()
        elif choice == '4':
            buy_blood(user_id)
        elif choice == '5':
            export_transaction(user_id)
        elif choice == '6':
            print("\nLogging out. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 8.")
