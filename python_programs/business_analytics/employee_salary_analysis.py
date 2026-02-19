num_of_employees = int(input("Enter the number of employees: "))
employee_data = {}

for i in range(num_of_employees):
    salary = float(input(f"Enter the salary of employee {i + 1}:  "))
    employee_data[i] = salary

total_salary = sum(employee_data.values())
average_salary = total_salary / num_of_employees
highest_salary = max(employee_data.values())
lowest_salary = min(employee_data.values())
employee_earning_above_average = [i for i, salary in employee_data.items() if salary > average_salary]

print(f"Total salary: {total_salary}")
print(f"Average salary: {average_salary}")
print(f"Highest salary: {highest_salary}")
print(f"Lowest salary: {lowest_salary}")
print(f"Employees earning above average: {len(employee_earning_above_average)}")
