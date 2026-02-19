def process_transactions(balance, num_transactions):
    total_deposits = 0
    total_withdrawals = 0
    failed_transactions = 0

    for i in range(num_transactions):
        print(f"\nTransaction {i + 1}:")
        transaction_type = input("Enter transaction type (deposit/withdraw): ").lower()

        if transaction_type not in ["deposit", "withdraw"]:
            print("Invalid transaction type.")
            continue

        amount = float(input("Enter the transaction amount: ₹"))

        if amount < 0:
            print("Invalid amount. Negative transactions are not allowed.")
            continue

        if transaction_type == "deposit":
            balance += amount
            total_deposits += amount

        elif transaction_type == "withdraw":
            if amount > balance:
                print("Transaction Failed: Insufficient funds.")
                failed_transactions += 1
            else:
                balance -= amount
                total_withdrawals += amount

        print(f"Current Balance: ₹{balance}")

    return balance, total_deposits, total_withdrawals, failed_transactions


# Main Program
initial_balance = float(input("Enter the initial account balance: ₹"))
number_of_transactions = int(input("Enter the number of transactions: "))

final_balance, deposits, withdrawals, failed = process_transactions(
    initial_balance, number_of_transactions
)

print("\nAccount Summary:")
print(f"Final Balance: ₹{final_balance}")
print(f"Total Deposits: ₹{deposits}")
print(f"Total Withdrawals: ₹{withdrawals}")
print(f"Failed Transactions: {failed}")
