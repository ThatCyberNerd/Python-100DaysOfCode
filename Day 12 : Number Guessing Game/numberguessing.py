import random
title = """

  ____  __ __    ___  _____ _____     ______  __ __    ___      ____   __ __  ___ ___  ____     ___  ____   __ 
 /    ||  |  |  /  _]/ ___// ___/    |      ||  |  |  /  _]    |    \ |  |  ||   |   ||    \   /  _]|    \ |  |
|   __||  |  | /  [_(   \_(   \_     |      ||  |  | /  [_     |  _  ||  |  || _   _ ||  o  ) /  [_ |  D  )|  |
|  |  ||  |  ||    _]\__  |\__  |    |_|  |_||  _  ||    _]    |  |  ||  |  ||  \_/  ||     ||    _]|    / |__|
|  |_ ||  :  ||   [_ /  \ |/  \ |      |  |  |  |  ||   [_     |  |  ||  :  ||   |   ||  O  ||   [_ |    \  __ 
|     ||     ||     |\    |\    |      |  |  |  |  ||     |    |  |  ||     ||   |   ||     ||     ||  .  \|  |
|___,_| \__,_||_____| \___| \___|      |__|  |__|__||_____|    |__|__| \__,_||___|___||_____||_____||__|\_||__|

"""

print(title)

print("Welcome To The Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1,100)
attempts = 0

valid_choice = False

while not valid_choice:
  difficulty = input("Choose a difficulty, easy or hard : ")
  
  if difficulty == "easy":
    attempts = 10
    print("You have 10 attempts.")
    valid_choice = True
  elif difficulty == "hard":
    attempts = 5
    print("You have 5 attempts.")
    valid_choice = True
  else:
    print("Enter a valid choice!")

number_guessed = False

while not number_guessed and attempts != 0:
  guess = int(input("Guess the number : "))
  
  if guess > number:
    print("Too High! Guess Again")
    attempts -= 1
    print(f"You have {attempts} attemtps left.")

  elif guess < number:
    print("Too Low! Guess Again")
    attempts -= 1
    print(f"You have {attempts} attemtps left.")

  elif guess == number:
    print("You have guessed the number, you won!")
    number_guessed = True

if attempts == 0:
  print("You ran out of attempts, you lost!")
  print(f"The number was {number}")
