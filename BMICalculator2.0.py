height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = float(weight / height ** 2)
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 24.9:
    print(f"Your BMI is {BMI}, you have a normal weight")
elif BMI < 29.9:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 34.9:
    print(f"Your BMI is {BMI}, you are Class 1 obese.")
elif BMI < 39.9:
    print(f"Your BMI is {BMI}, you are Class 2 obese.")
else:
    print(f"Your BMI is {BMI}, you are Class 3 obese.")
