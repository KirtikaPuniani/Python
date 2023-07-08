print("Welcome to Pizza Deliveries!!")
Size = input("Please tell the size of pizza you want to order? Small or Medium or Large?")
Pepperoni = input("Do you want pepperoni? Y or N?")
Extra_Cheese = input ("Do you want extra cheese? Y or N?")
bill = 0

if Size == "Small":
    bill += 200
elif Size == "Medium":
    bill += 350
else:
    bill += 500

if Pepperoni == "Y":
    if Size == "Small":
        bill += 50
    else:
        bill += 75
if Extra_Cheese == "Y":
    if Size == "Small":
        bill += 50
    else:
        bill += 75

print(f"Your final bill is Rs {bill}")
