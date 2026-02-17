number_of_customers = int(input("Enter the number of customers: "))
customer_spending = {}
for i in range(number_of_customers):
    spending = float(input(f"Enter the spending of customer {i + 1}: "))
    customer_spending[i] = spending
    
    if spending > 10000:
        print(f"Customer {i + 1} is a Higvalue")
    elif 5000<spending <= 9999:
        print(f"Customer {i + 1} is a Midvalue")
    else:
        print(f"Customer {i + 1} is a Lowvalue")
   
total_revenue = sum(customer_spending.values())
average_spending = total_revenue / number_of_customers
number_of_highvalue_customers = sum(1 for spending in customer_spending.values() if spending > 10000)
number_of_midvalue_customers = sum(1 for spending in customer_spending.values() if 5000 < spending <= 9999)
number_of_lowvalue_customers = sum(1 for spending in customer_spending.values() if  spending <= 5000)   

print(f"Total revenue: {total_revenue}")
print(f"Average spending: {average_spending}")
print(f"Number of highvalue customers: {number_of_highvalue_customers}")
print(f"Number of midvalue customers: {number_of_midvalue_customers}")
print(f"Number of lowvalue customers: {number_of_lowvalue_customers}")