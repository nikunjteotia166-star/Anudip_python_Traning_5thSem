p = int(input("enter principal Amount:"))
r = int(input("enter rate of interest:"))
t = int(input("enter time:"))

if p>0 and r>0 and t>0:
    si = (p*r*t)/100
    print("simple interest =",si)

else:
    print("invalid input! values must be positive.")