number_of_expenses = int(input("Enter the number of expenses: "))
expenses = []

for i in range(number_of_expenses):
    expense_amount = float(input(f"Enter the expense for expense {i + 1}: "))
    expenses.append(expense_amount)
    
    if expense_amount >= 10000:
        print("Expense is  high")
    elif 5000<expense_amount<10000:
        print("Expense is  Medium.")
    elif expense_amount < 5000:       
        print("Expense is low.")   
    elif expense_amount < 0:
        print("Expense cannot be negative. Please enter a valid amount.")
        expenses.pop()
    else:
        print("Expense is invalid.")
    
total_expenses = sum(expenses)
average_expense = total_expenses / number_of_expenses
highest_expense = max(expenses)
lowest_expense = min(expenses)
number_of_expenses_above_average = sum(1 for expense in expenses if expense > average_expense)
# number_of_expenses_below_average = sum(1 for expense in expenses if expense < average_expense)

print(f"\nExpense Summary Report:")
print(f"Expenses: {expenses}")
print(f"Total expenses: {total_expenses:.2f}")
print(f"Average expense: {average_expense:.2f}")
print(f"Highest expense: {highest_expense:.2f}")
print(f"Lowest expense: {lowest_expense:.2f}")

print(f"\nCategory")
for i, expense in enumerate(expenses):
    if expense > average_expense:
        print(f"Expense {i + 1}: High")
    elif expense < average_expense:
        print(f"Expense {i + 1}: Low")
    else:
        print(f"Expense {i + 1}: Medium")
        
print(f"Number of expenses above average: {number_of_expenses_above_average}")
# print(f"Number of expenses below average: {number_of_expenses_below_average}")

