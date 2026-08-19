rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

# first, the player choice for rock, paper or scissor

player_choice = int(input("Choose 0 for Rock, 1 for Paper and 2 for Scissors: "))

#printing the choice

if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)
else:
    print("Please play a valid form. ")
    quit()

# printing the computer choice

print("Computer chose:\n")

pc_choice = random.randint(0, 2)

if pc_choice == 0:
    print(rock)
elif pc_choice == 1:
    print(paper)
elif pc_choice == 2:
    print(scissors)

# now, the comparison

if player_choice == pc_choice:
    print("It's a draw.")
elif (player_choice - pc_choice) % 3 == 1:
    print("You win.")
else:
    print("You lose.")
    