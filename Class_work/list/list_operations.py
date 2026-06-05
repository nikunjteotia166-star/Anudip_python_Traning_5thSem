# Create an empty list
numbers = []

# Take 20 numbers from the user
for i in range(7):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Display original list
print("Original List:", numbers)

# Number whose duplicates are to be removed
x = int(input("Enter a number: "))

count = 0

# Create a new list
new_list = []

for num in numbers:
    if num == x:
        count += 1
        if count == 1:      # Keep first occurrence
            new_list.append(num)
    else:
        new_list.append(num)

# Display updated list
print("Updated List:", new_list)