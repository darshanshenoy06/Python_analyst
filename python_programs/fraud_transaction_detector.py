def analyze_risk(transactions):
    high_risk = 0
    medium_risk = 0
    low_risk = 0

    for amount in transactions:
        if amount >= 50000:
            high_risk += 1
        elif 10000 <= amount < 50000:
            medium_risk += 1
        else:
            low_risk += 1

    return high_risk, medium_risk, low_risk


try:
    number_of_transactions = int(input("Enter the number of transactions: "))

    if number_of_transactions <= 0:
        print("No transactions to analyze.")
    else:
        transactions = []

        for i in range(number_of_transactions):
            transaction = float(input(f"Enter the transaction for transaction {i + 1}: "))
            transactions.append(transaction)

        high, medium, low = analyze_risk(transactions)

        print("\nRisk Summary Report:")
        print("Number of High Risk transactions:", high)
        print("Number of Medium Risk transactions:", medium)
        print("Number of Low Risk transactions:", low)

except ValueError:
    print("Invalid input! Please enter numeric values only.")
except Exception as e:
    print(f"An error occurred: {e}")