p = 0
a = 0
for i in range(30):
    s =input("enter p for present students and a for absent students:").upper()

    if s== "P":
        p = p+1
    else:
        a = a+1

print("present students:" , p)
print("absent students:" , a)