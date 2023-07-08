year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100:
        if year % 400:
            print("Year is a leap year")
        else:
            print("Year is not a leap year")
    else:
        print("Year is a leap year")
else:
    print("Year is not a leap year")
