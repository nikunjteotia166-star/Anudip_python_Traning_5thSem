#program to check three angles form a triangle or not
#define type of triangle
angle1=float(input("eneter the first angle:"))
#validate angle 1
if(angle1<=0):
    exit("angle must be positive")
#-------------------------------------------
angle2=float(input("eneter the second angle:"))
#validate angle 2
if(angle2<=0):
    exit("angle must be positive")
#-------------------------------------------
angle3=float(input("eneter the third angle:"))
#validate angle 3
if(angle3<=0):
    exit("angle must be positive")
#-------------------------------------------
#verifying triangle formation
if(angle1+angle2+angle3==180):
    #triangle is formed
    #acute angle triangle
    if(angle1 < 90 and angle2 < 90 and angle3 < 90):
        print("above angles form acute angle triangle")
    elif(angle1 == 90 or angle2 == 90 or angle3 == 90):
        print("above angles form right angle triangle")
    else:
        print("above angle forms obtuse angle triangle")



else:
    print("above angles do not form any triangle")