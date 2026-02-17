my_list = []

for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    my_list.append(num)
print(f"The list of numbers you entered is: {my_list}")
print(f"The sum of the numbers is: {sum(my_list)}")
print(f"The average of the numbers is: {sum(my_list) / len(my_list)}")    
print(f"The maximum number is: {max(my_list)}")
print(f"The minimum number is: {min(my_list)}")