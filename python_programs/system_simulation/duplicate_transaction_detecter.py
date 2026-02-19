try:
        number_of_transactions = int(input("Enter the number of transactions: "))
        transactions = []
        for i in range(number_of_transactions):
            transaction_id = input(f"Enter the transaction for transaction {i + 1}: ")
            
            transactions.append(transaction_id)
            
            
            total_transactions = len(transactions)
            unique_transactions = len(set(transactions))
            duplicate_transactions = [t for t in set(transactions) if transactions.count(t) > 1]
            number_of_duplicate_transactions = sum(transactions.count(t) - 1 for t in set(transactions))
            
        print(f"fraud Summary Report:")
        print(f"Total Transactions: {total_transactions}")
        print(f"Unique Transactions: {unique_transactions}")
        print(f"Duplicate Transactions: {duplicate_transactions}")
        print(f"Number of Duplicate Transactions: {number_of_duplicate_transactions}")
            
except ValueError:
    print("Invalid input! Please enter numeric values only.")
except Exception as e:
    print(f"An error occurred: {e}")            