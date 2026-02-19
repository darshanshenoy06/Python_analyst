number_of_transactions = int(input("Enter the number of transactions: "))
transaction_amounts = []

risk_levels = ["Low", "Medium", "High"]

# Step 1: Collect transaction amounts
for i in range(number_of_transactions):
    amount = float(input(f"Enter amount for transaction {i + 1}: "))
    transaction_amounts.append(amount)


def calculate_risk_score(transactions):
    total_risk_score = 0

    # Calculate total risk score
    for transaction_amount in transactions:
        if transaction_amount > 50000:
            total_risk_score += 3
        elif 20000 <= transaction_amount <= 50000:
            total_risk_score += 2
        else:
            total_risk_score += 1

    # Count high-risk transactions
    number_of_high_risk_transactions = sum(
        1 for amount in transactions if amount > 50000
    )

    # Final risk level (FinTech logic)
    if number_of_high_risk_transactions > 3:
        final_risk_level = "High"
    elif total_risk_score >= 10:
        final_risk_level = "Medium"
    else:
        final_risk_level = "Low"

    return total_risk_score, number_of_high_risk_transactions, final_risk_level


# Step 2: Call function properly
total_score, high_risk_count, final_level = calculate_risk_score(transaction_amounts)

# Step 3: Output summary
print("\nFraud Risk Analysis Report:")
print(f"Transaction Amounts: {transaction_amounts}")
print(f"Total Risk Score: {total_score}")
print(f"Number of High-Risk Transactions (> 50000): {high_risk_count}")
print(f"Final Risk Level: {final_level}")
