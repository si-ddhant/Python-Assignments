gInc = float(input("enter your gross income"))
dep = int(input("enter no. of dependants"))

rate= 0.2
std_ded= 10000

taxable_income = gInc - std_ded - (dep*3000)

tax= taxable_income*rate
print(tax)