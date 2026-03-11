number_of_transactions = input("Enter the number of transactions: ")
transactions = ("user_id ,amount ,category",)

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
    category_percentages = {category: (total / total_transaction_amount * 100) if total_transaction_amount > 0 else 0 for category, total in category_totals.items()} 
    return category_totals, category_percentages, average_transaction_amount, highest_transaction, lowest_transaction, num_of_high_value_transactions
analyze_transactions(transactions)