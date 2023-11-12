from datetime import datetime

def print_red(text):
    return f"\033[91m{text}\033[0m"
def print_blue(text):
    return f"\033[94m{text}\033[0m"
def print_yellow(text):
    return f"\033[93m{text}\033[0m"

def export_transaction(user_id):
    try:
        current_date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"transactions-user-{current_date}{user_id}.txt"

        with open("database/bloodBuy.txt", "r") as transactions_file:
            user_transactions = [line for line in transactions_file if f"User ID: {user_id}," in line]

            if user_transactions:
                with open(file_name, "w") as file:
                    file.write("Transaction Report\n\n")
                    for transaction in user_transactions:
                        transaction_info = transaction.strip().split(", ")
                        formatted_transaction = "\n".join(transaction_info)
                        
                        file.write(f"{(formatted_transaction)}\n\n")
                    
                    print(print_blue(f"\nTransaction report exported successfully. File: {file_name}"))
            else:
                print(print_yellow("\nNo transactions found for the user."))
    except IOError:
        print(print_red("\nError: Unable to export the transaction report."))
