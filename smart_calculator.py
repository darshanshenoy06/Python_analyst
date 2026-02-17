print("Select Operation:")
print("1 -> Add")
print("2 -> Subtract")
print("3 -> Multiply")
print("4 -> Divide")

choice = int(input("Enter your choice (1/2/3/4): "))

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if choice == 1:
    result = number1 + number2
    print(f"The sum of {number1} and {number2} is: {result}")
elif choice == 2:
    result = number1 - number2
    print(f"The difference of {number1} and {number2} is: {result}")
elif choice == 3:
    result = number1 * number2
    print(f"The product of {number1} and {number2} is: {result}")
elif choice == 4:
    if number2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = number1 / number2
        print(f"The division of {number1} and {number2} is: {result}")
else:
    print("Invalid choice. Please select a valid operation (1/2/3/4).")