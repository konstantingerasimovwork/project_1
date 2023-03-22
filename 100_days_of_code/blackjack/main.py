from art import logo
import random
from replit import clear 


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(cards)
  return random_card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  elif user_score == computer_score:
    return "It's a draw!"
  elif computer_score == 0:
    return "User lose!"
  elif user_score == 0:
    return "User win!"
  elif user_score > 21:
    return"User lose!"
  elif computer_score > 21:
    return"Computer lose!"
  elif user_score > computer_score:
    return "User win!"
  else: 
    print("You lose!")



def play_the_game():
  print(logo)

  
  user_cards = []
  computer_cards = []
  game_over = False
  for i in range(0, 2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  
  
  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score {user_score}")
    print(f"Computer cards: {computer_cards}, current score {computer_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:  
      game_over = True
    else:  
      continue_game = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if continue_game == "y":
        user_cards.append(deal_card())
      else: 
        game_over = True
      
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  
while input("Do you want to play the game? Type 'y' or 'n' ").lower() == "y":
  clear()
  play_the_game()