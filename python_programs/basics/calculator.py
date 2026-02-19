first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))


sum_number = first_number + second_number
difference_number = first_number - second_number
product_number = first_number * second_number
division_number = first_number / second_number  

if second_number == 0:
    division_number = "undefined (cannot divide by zero)"

print(f"The sum of {first_number} and {second_number} is: {sum_number}")
print(f"The difference of {first_number} and {second_number} is: {difference_number}")
print(f"The product of {first_number} and {second_number} is: {product_number}")
print(f"The division of {first_number} and {second_number} is: {division_number}")