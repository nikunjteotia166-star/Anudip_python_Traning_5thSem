# Input marks of 5 subjects

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))

# Calculate total marks
total = m1 + m2 + m3 + m4 + m5

# Calculate percentage
percentage = total / 5

# Count failed subjects (less than 40 marks)
fail_count = 0

if m1 < 40:
    fail_count += 1
if m2 < 40:
    fail_count += 1
if m3 < 40:
    fail_count += 1
if m4 < 40:
    fail_count += 1
if m5 < 40:
    fail_count += 1

# Find grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

# Display result
print("Total Marks =", total)
print("Percentage =", percentage)
print("Grade =", grade)
print("Number of Subjects Failed =", fail_count)