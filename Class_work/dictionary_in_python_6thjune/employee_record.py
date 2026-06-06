# Create an empty dictionary
employees = {}

# Input Employee ID and Salary for 10 employees
for i in range(10):
    emp_id = input("Enter Employee ID: ")
    salary = int(input("Enter Salary: "))
    
    # Store Employee ID as key and Salary as value
    employees[emp_id] = salary

# Variable to count employees having salary greater than 30000
count = 0

print("\nEmployees having salary below 20000:")

# Traverse dictionary
for emp_id, salary in employees.items():
    
    # Count employees with salary > 30000
    if salary > 30000:
        count += 1
    
    # Display employees with salary < 20000
    if salary < 20000:
        print("Employee ID:", emp_id, "Salary:", salary)

# Display total count
print("\nTotal employees having salary greater than 30000 =", count)