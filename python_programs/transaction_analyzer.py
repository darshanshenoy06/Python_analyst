num_transactions = int(input("How many transactions occured today :"))
amounts = []
for i in range(num_transactions):
    amount = float(input(f"Enter the amount for transaction {i + 1}: "))
    amounts.append(amount)
    
    # if amount>0:
    #     print(f"Transaction {i + 1} is a credit of {amount}")
    # elif amount<0:
    #     print(f"Transaction {i + 1} is a debit of {amount}")

total_balance_change = sum(amounts)
total_deposit_amount = sum(amount for amount in amounts if amount > 0)
total_withdrawal_amount = sum(amount for amount in amounts if amount < 0)
number_of_deposits = sum(1 for amount in amounts if amount > 0)
number_of_withdrawals = sum(1 for amount in amounts if amount < 0)
largest_deposit = max((amount for amount in amounts if amount > 0), default=0)
largest_withdrawal = min((amount for amount in amounts if amount < 0), default=0)


print(f"\nTransaction:{amounts}")
print(f"The total balance change for the day is: {total_balance_change}")
print(f"The total deposit amount is: {total_deposit_amount}")
print(f"The total withdrawal amount is: {total_withdrawal_amount}")
print(f"The number of deposits is: {number_of_deposits}")
print(f"The number of withdrawals is: {number_of_withdrawals}")
print(f"The largest deposit is: {largest_deposit}")
print(f"The largest withdrawal is: {largest_withdrawal}")