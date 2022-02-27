#q1
def TowerofHanoi(n,source,dest,middle):
    if(n<1):
        print("not possible")
        return
    if(n==1):
        print("move disk{} from {} to {} ".format(n,source,dest))
        return
    TowerofHanoi(n-1,source,middle,dest)
    print("move disk {} from {} to{}".format(n,source,dest))
    TowerofHanoi(n-1,middle,dest,source)
n=int(input("enter the number of disk"))
TowerofHanoi(n,"A","C","B")
#q2
# pascal triangle using loop
def pascaltriangle(rows):
    for i in range(0,rows):
        for j in range(0,i+1):
            print(getnumber(i,j),end=" ")
        print()

def getnumber(x,y):
    num=1
    if y>x-y:
        y=x-y
    for i in range(0,y):
        num=num*(x-i)
        num=num//(i+1)

    return num    
pascaltriangle(5)

# pascal triangle using recursive
class solution:
    def generates(self,num_rows):
        if num_rows==0:
            return []
        if num_rows==1:
            return[[1]]

        new_row = [1]
        result=self.generate(num_rows-1)
        last_row=result[-1]
        for i in range(len(last_row)-1):
            num=last_row[i]+last_row[i+1]
            new_row.append(num)

        new_row.append(1)
        result.append(new_row)
        return result




#q3
int1, int2 = map(int,input("Enter 2 numbers: ").split())
Quotient = int1 // int2
Remainder = int1 % int2
print("Part a")
print("a. Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))
print("Part b")
if (Quotient == 0):
    print("<b> The quotient is zero")
if (Remainder == 0):
    print("<b> The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("<b> All the values are non zero")
print("Part c")
partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]
result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f"<c> Filtered out numbers that are greater than 4 are : {result}")
print("Part d")
setresult = set(result)
print("<d> Set:",setresult)
print("Part e")
immutableSet = frozenset(setresult) 
print("<e> Immutable set:",immutableSet)
print("Part f")
print("<f> Hash value of the max value from the above set:", hash(max(immutableet)))
# q4
class Student:
    def __init__(self, student, roll_no):
        self.name = student
        self.roll_no = roll_no

    def __del__(self):
        print("object deleted")


student1 = Student("Raman deep singh",21103003) # CREATING OBJECT
print("Object created")
print(f"The name of the student is {student1.name} and SID is {student1.roll_no}.")
del student1# deleting object
#q5
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
#creating employee Object
employee1 = Employee("Muskaan", 30000)
employee2 = Employee("Ashok", 320000)
employee3 = Employee("Viren", 90000)
# updating salary
employee1.salary = 70000
print("(a) The updated salary of Mehak is 70000 ")
# deleting a record
print("(b) Record of Viren deleted")
del employee3



        
