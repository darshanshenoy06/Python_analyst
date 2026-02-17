numbers = []


for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
squres = [num ** 2 for num in numbers]
print(f"The list of numbers you entered is: {numbers}")
print(f"The list of squares of the numbers are: {squres}")