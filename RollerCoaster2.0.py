print("Welcome to the Rollercoaster ride!!")
height = int(input("What is the height in cm?"))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is the age of the person?"))
    if age < 12:
        print("Price of ticket is 50 Rs")
    elif age <= 18:     #over 12 and under 18
        print("Price of ticket is 100 Rs")
    else:               #everybody else over 18
        print("Price of ticket is 200 Rs")
else:
    print("Apologies! You can't ride the rollercoaster")
