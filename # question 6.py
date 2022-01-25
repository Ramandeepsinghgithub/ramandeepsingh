#q 6
a=int(input("Enter first side of triangle"))
b=int(input("Enter second side of triangle"))
c=int(input("Enter third side of triangle"))
if((a+b)>c and (b+c)>a and (c+a)>b and a>0 and b>0 and c>0):
    print("yes")
else:
    print("No")
