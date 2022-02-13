#q1
string=input("Enter any string:")
c=input("Enter character to check frequency:")
count=0
for i in string:
    if i==c:
        count+=1
print(c,"occurs ",count,"times")        
#q2
string=input("Enter any string:")
c=input("Enter character to check frequency:")
count=0
for i in string:
    if i==c:
        count+=1
print(c,"occurs ",count,"times")        
   else:
         print("invalid date")
elif(month==2):
    year=int(input("Give year-"))
    if(1800<=year<=2025):
        day=int(input("Give day-"))
        if(year%4==0):
            if(1<=day<=29):
                print("Date-",day,"/",month,"/",year)
                if(day==29):
                    print("Next Date-","1/",month+1,"/",year)
                else:
                    print("Next Date-",day+1,"/",month,"/",year)              
            else:
                print("invalid day")
        else:
            if(1<=day<=28):
                print("Date-",day,"/",month,"/",year)
                if(day==28):
                    print("Next Date-","1/",month+1,"/",year)
                else:
                    print("Next Date-",day+1,"/",month,"/",year)       
            else:
                print("invalid day")     
    else:
        print("invalid year")
else:
    print("invalid month")
   #q3
a=int(input("Enter 1 nummbe:"))
b=int(input("Enter 2 number:"))
c=int(input("Enter 3 number:"))
a=[(x,x**2) for x in (a,b,c)]
print(a)
#q4


Grade_points=int(input("Give a number between 4 and 10 including them-"))
if(Grade_points==4):
    print("Performance=Poor")
    print("Letter Grade=D")
elif(Grade_points==5):
    print("Performance=Below Average")
    print("Letter Grade=C")
elif(Grade_points==6):
    print("Performance=Average")
    print("Letter Grade=C+")
elif(Grade_points==7):
    print("Performance=Good")
    print("Letter Grade=B")
elif(Grade_points==8):
    print("Performance=Very Good")
    print("Letter Grade=B+")
elif(Grade_points==9):
    print("Performance=Excellent")
    print("Letter Grade=A")
elif(Grade_points==10):
    print("Performance==Outstanding")
    print("Letter Grade=A+")
else:
    print("error")
#q5

Word="ABCDEFGHIJK"

counter=1

while(counter<7):
    print(" "*(counter-1),Word[0:11-((counter-1)*2)])
    counter=counter+1

#q7
n=int(input("enter a number:"))
x=0
y=1
z=0
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y
average=z/n
print(average)
#q8
s1={1,2,3}
s2={2,4,6,8}
s3={1,5,9,13,17}
#a
set=s1^s2
print(set)
#b
s1={1,2,3}
s2={2,4,6,8}
s3={1,5,9,13,17}
set=s1^(s2^s3)
print(set)
#c
set=(s1&s2)|(s2&s3)|(s1&s3)
print(set)
#d
newset={1,2,3,4,5,6,7,8,9,10}
set=newset-s1
print(set)
#e
set=newset-(s1|s2|s3)
print(set)
