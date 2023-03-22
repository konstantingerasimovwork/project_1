import random
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

game = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice <= 2 and player_choice >= 0:
  print(game[player_choice])
  random_choice = random.randint(0, 2)
  print(game[random_choice])
  if player_choice == 0 and random_choice == 2:
    print("You win!")
  elif player_choice == 2 and random_choice == 1:
    print("You win")
  elif player_choice == 1 and random_choice == 0:
    print("You win")
  elif player_choice == random_choice:
    print("It's a draw")
  else:
    print("You lose!")
else: 
  print("You typed an invalid number, you lose!")