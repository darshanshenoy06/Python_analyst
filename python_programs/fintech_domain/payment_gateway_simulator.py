initial_wallet_balance = float(input("Enter the initial wallet balance: ₹"))
number_of_payment_requests = int(input("Enter the number of payment requests: "))
payment_requests = []

for i in range(number_of_payment_requests):
    amount = float(input(f"Enter the amount for payment request {i + 1}: ₹"))
    payment_requests.append(amount)


def process_payment_requests(balance, payments):
    successful_count = 0
    failed_count = 0
    suspicious_transactions = []

    for i, payment in enumerate(payments, 1):

        if payment < 0:
            print(f"Payment {i}: Invalid Transaction (Negative amount)")
            failed_count += 1
            continue

        if payment > 100000:
            print(f"Payment {i}: Suspicious Transaction of ₹{payment}")
            suspicious_transactions.append(payment)

        if payment <= balance:
            print(f"Payment {i}: Payment Successful")
            balance -= payment
            successful_count += 1
        else:
            print(f"Payment {i}: Payment Failed (Insufficient Funds)")
            failed_count += 1

    return balance, successful_count, failed_count, suspicious_transactions


final_balance, successful_payment_count, failed_payment_count, suspicious_transactions_list = process_payment_requests(
    initial_wallet_balance, payment_requests
)

print("\nPayment Summary:")
print(f"Final Wallet Balance: ₹{final_balance}")
print(f"Successful Payments: {successful_payment_count}")
print(f"Failed Payments: {failed_payment_count}")
print(f"Suspicious Transactions: {suspicious_transactions_list}")
