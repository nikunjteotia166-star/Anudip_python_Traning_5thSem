# Program to calculate Area and Perimeter of a Rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

# Validation
if length <= 0 or breadth <= 0:
    print("Invalid Input! Length and Breadth must be greater than 0.")
else:
    area = length * breadth
    perimeter = 2 * (length + breadth)

    print("Area of Rectangle =", area)
    print("Perimeter of Rectangle =", perimeter)