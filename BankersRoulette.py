import random

names_string = input("Give the names of people out for dinner")
names = names_string.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items-1)
person_who_will_pay_the_bill = names[random_choice]

print(person_who_will_pay_the_bill + " is going to buy the meal today!!")
