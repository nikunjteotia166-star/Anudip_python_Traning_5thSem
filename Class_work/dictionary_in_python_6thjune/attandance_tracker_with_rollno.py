# Create an empty dictionary to store attendance
attendance = {}

# Input attendance of 30 students
for i in range(30):
    roll_no = int(input("Enter Roll Number: "))
    status = input("Enter Attendance (Present/Absent): ")

    # Store roll number as key and attendance as value
    attendance[roll_no] = status

# Display roll numbers of present students
print("\nStudents who are Present:")

for roll_no in attendance:
    if attendance[roll_no].lower() == "present":
        print(roll_no)