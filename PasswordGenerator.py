import random
Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
NR_Letters = int(input("How many letters would you like in your password?\n"))
NR_Symbols = int(input(f"How many symbols would you like?\n"))
NR_Numbers = int(input(f"How many numbers would you like?\n"))

#Easy Method
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard/Better Method
Password_List = []

for char in range(1, NR_Letters + 1):
  Password_List.append(random.choice(Letters))

for char in range(1, NR_Symbols + 1):
  Password_List += random.choice(Symbols)

for char in range(1, NR_Numbers + 1):
  Password_List += random.choice(Numbers)

print(Password_List)
random.shuffle(Password_List)
print(Password_List)

password = ""
for char in Password_List:
  password += char
