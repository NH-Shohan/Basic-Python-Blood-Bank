def print_red(text):
    return f"\033[91m{text}\033[0m"

def view_all_transactions():
    try:
        with open("database/bloodBuy.txt", "r") as file:
            transactions = file.readlines()

        if transactions:
            print("\nAll Transactions:\n")
            for transaction in transactions:
                print(transaction.strip())
        else:
            print("\nNo transactions found.")
    except IOError:
        print(print_red("\nError: Unable to access transaction records."))