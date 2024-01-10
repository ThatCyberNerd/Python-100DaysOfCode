import random 
import subprocess, sys

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False 
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
      return 0
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)  
    return sum(cards)
  
  def compare(user_score, computer_score):
    if user_score == computer_score:
      return "It's a draw!"
    elif user_score == 0:
      return "You Win with a BlackJack!"
    elif computer_score == 0:
      return "You Lose. Computer has a BlackJack!"
    elif user_score > 21:
      return "You Lose. You crossed the BlackJack!"
    elif computer_score > 21:
      return "You Win. Opponent crossed the BlackJack!"
    elif user_score > computer_score:
      return "You Win!"
    else:
      return "You Lose!"
  
  while not is_game_over:
  
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
  
    print(f"User Cards : [{user_cards}], Current Score : {user_score}")
    print(f"Computer First Card : [{computer_cards[0]}]")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_deal = input("Type y to get another card, Type n to pass")
      if user_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"Your Final Hand : {user_cards}, Your Final Score : {user_score}")
  print(f"Opponent's Final Hand : {computer_cards}, Opponent's Final Score : {computer_score}")
  print(compare(user_score, computer_score))

while input("Do You Want To Play A Game Of BlackJack? ") == "y":
  subprocess.run('clear', shell=True)
  print(logo)
  play_game()
  
