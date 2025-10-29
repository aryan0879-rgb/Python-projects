# simple calculator
a=int(input("enter your first number: "))
b=int(input("enter your second number: "))
print("addition =", a+b)
print("subtraction=", a-b)
print("division=", a/b)
print("mulptiplication=", a*b)
# tip calculator
c=float(input("your bill amount: "))
d=float(input("tip in % =  "))
if c<0 or d<0:
    raise ValueError("amount or tip % must be positive numbers")
print("total amount=", c+(c*d)/100)