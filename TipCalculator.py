print("Welcome to Tip Calculator!!")

bill =  float(input("What is the total bill for today?"))
tip = int(input("What is the percentage of the tip you wanna give? 10, 12 or 15?"))
people = int(input("How many people are splitting the bill?"))

tip_as_percent = tip/100
total_tip_amount = bill * tip/100
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person)

print(f"Each person should pay: INR {final_amount}")
