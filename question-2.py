#Q 2 To compute a person's income tax (in $)
Tax=0
GI=0
SD=10000
DD=3000
TI=0
GI=int(input("Enter Gross Income"))
ND=int(input("Enter No. of Dependent"))
TI=GI-SD-(DD*ND)
print("Taxable Income:",TI)
TAX=(TI*20)/100
print("Total Tax to be paid:",Tax)

