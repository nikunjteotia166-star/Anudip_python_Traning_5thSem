# List of marks
marks = [78, 45, 92, 35, 88, 40, 99, 56]

# List for passed students
passed_students = []

# Count failed students
failed_count = 0

# Highest and lowest marks
highest = marks[0]
lowest = marks[0]

# Merit list (marks above 75)
merit_list = []

# Loop through the list
for mark in marks:

    # Passed students
    if mark >= 40:
        passed_students.append(mark)
    else:
        failed_count += 1

    # Find highest marks
    if mark > highest:
        highest = mark

    # Find lowest marks
    if mark < lowest:
        lowest = mark

    # Merit list
    if mark > 75:
        merit_list.append(mark)

# Display results
print("Passed Students:", passed_students)
print("Failed Count:", failed_count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit_list)