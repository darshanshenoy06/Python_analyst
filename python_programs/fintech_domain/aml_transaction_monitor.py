num_of_transaction_per_day = int(input("Enter the number of transactions per day: "))
transaction_amounts = []

for i in range(num_of_transaction_per_day):
    amount = float(input(f"Enter the amount for transaction {i + 1}: ₹"))
    transaction_amounts.append(amount)


def aml_monitor(transactions):
    total_transaction_amount = sum(transactions)
    number_of_large_transactions = sum(1 for amt in transactions if amt > 100000)
    transaction_count = len(transactions)

    # AML Risk Logic
    if total_transaction_amount > 250000:
        risk_level = "High Risk Account"
    elif transaction_count > 3 or number_of_large_transactions > 0:
        risk_level = "Medium Risk"
    else:
        risk_level = "Low Risk"

    return total_transaction_amount, number_of_large_transactions, risk_level


total, large_txns, risk = aml_monitor(transaction_amounts)

print("\nAML Transaction Monitoring Report:")
print(f"Total Transaction Amount: ₹{total}")
print(f"Number of Large Transactions (> ₹1,00,000): {large_txns}")
print(f"Daily Transaction Count: {len(transaction_amounts)}")
print(f"Risk Classification: {risk}")
