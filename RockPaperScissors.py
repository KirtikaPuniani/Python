import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [Rock, Paper, Scissors]

Player_Choice = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors\n"))
print(game_images[Player_Choice])

Computer_Choice = random.randint(0, 2)
print("Computer Chose:")
print((game_images[Computer_Choice]))

if Player_Choice >= 3 or Player_Choice < 0:
    print(("You have typed invalid choice, You Loose!"))
elif Player_Choice == 0 or Player_Choice == 2:
    print(("You Win!!!"))
elif Computer_Choice == 0 or Computer_Choice == 2:
    print(("You Loose!!!"))
elif Player_Choice > Computer_Choice:
    print(("You Win!!!"))
elif Computer_Choice == Player_Choice:
    print(("It's a Draw!!!"))
