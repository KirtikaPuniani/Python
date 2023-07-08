print("Welcome to the Rollercoaster ride!!")
height = int(input("What is the height in cm?"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is the age of the person?"))
    if age < 12:
        bill =50
        print("Child tickets are 50 Rs")
    elif age <= 18:     #over 12 and under 18
        bill = 100
        print("Youth tickets are 100 Rs")
    else:               #everybody else over 18
        bill = 200
        print("Adult tickets are 200 Rs")

    wants_photo = input("Do you want a photo taken? Y or N?")
    if wants_photo == "Y":
        bill += 50
    print(f"Your final bill is {bill}")

else:
    print("Apologies! You can't ride the rollercoaster")
