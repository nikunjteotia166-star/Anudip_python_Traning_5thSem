
# 1 = Booked, 0 = Available
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

booked = 0
available = 0
available_seats = []

# Count booked and available seats
for seat in seats:
    if seat == 1:
        booked += 1
    else:
        available += 1

print("Booked Seats:", booked)
print("Available Seats:", available)

# Find first available seat
for i in range(len(seats)):
    if seats[i] == 0:
        print("First Available Seat:", i + 1)
        break

# Create list of all available seat numbers
for i in range(len(seats)):
    if seats[i] == 0:
        available_seats.append(i + 1)

print("Available Seat Numbers:", available_seats)

# Calculate occupancy percentage
occupancy = (booked / len(seats)) * 100

print("Bus Occupancy:", occupancy, "%")

# Check if occupancy is more than 70%
if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")



