# Program to check whether a number is a Strong Number

num = int(input("Enter a number: "))

original_num = num 

sum_fact = 0

# Process each digit of the number
while num > 0:
    digit = num % 10      # Extract last digit

    # Calculate factorial of the digit
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    # Add factorial to the sum
    sum_fact = sum_fact + fact

    # Remove the last digit
    num = num // 10

# Check whether the number is Strong Number or not
if sum_fact == original_num:
    print(original_num, "is a Strong Number")
else:
    print(original_num, "is not a Strong Number")