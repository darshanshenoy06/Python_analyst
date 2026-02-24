num_of_transactions = input("Enter the number of transactions: ")
transactions = []
for i in range(int(num_of_transactions)):
    transaction = input(f"Enter transaction {i+1} (format: amount category): ")
    amount, category = transaction.split()
    transactions.append((float(amount), category))
def analyze_transactions(transactions):
    category_totals = {}
    for amount, category in transactions:
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    total_transaction_amount = sum(category_totals.values())
    average_transaction_amount = total_transaction_amount / len(transactions) if transactions else 0
    highest_transaction = max(transactions, key=lambda x: x[0]) if transactions else (0, "") 
    lowest_transaction = min(transactions, key=lambda x: x[0]) if transactions else (0, "")   
    num_of_high_value_transactions = sum(1 for amount, _ in transactions if amount > average_transaction_amount)    
    category_percentages = {category: (total / total_transaction_amount) * 100 for category, total in category_totals.items()}
    return category_totals, category_percentages, average_transaction_amount, highest_transaction, lowest_transaction, num_of_high_value_transactions
category_totals, category_percentages, average_transaction_amount, highest_transaction, lowest_transaction, num_of_high_value_transactions = analyze_transactions(transactions)
 
print(f"Average transaction amount: {average_transaction_amount}")
print(f"Highest transaction: {highest_transaction}")
print(f"Lowest transaction: {lowest_transaction}")
print(f"Number of high-value transactions: {num_of_high_value_transactions}")
