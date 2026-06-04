rate = 10          # liters per minute
water = 0
capacity = 100

while water < capacity:
    water += rate
#------------------------------------------
    if water > capacity:      # validation
        water = capacity

    print("Water in tank:", water, "liters")
#-----------------------------------------
print("Tank is full.")

