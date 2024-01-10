logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

print(logo)
print("HOW WELL DO YOU KNOW THE INSTAGRAM FOLLOWER COUNT OF CELEBRITIES?")
from game_data import data
import sys, subprocess

game_completed = False
score = 0
i=0

while not game_completed and i < 50:

  print(f"Compare A : {data[i]['name']}, a {data[i]['description']} from {data[i]['country']}")
  print(vs)
  print(f"Against B : {data[i+1]['name']}, a {data[i+1]['description']} from {data[i+1]['country']}")
  answer = input("Who has more followers? A or B? ")
  
  if answer == "A":
    if data[i]['follower_count'] > data[i+1]['follower_count']:
      score += 1
      subprocess.run('clear', shell=True)
      print(logo)
      print(f"You're Right! Current Score = {score}")
      i += 1
    else:
      subprocess.run('clear', shell=True)
      print(logo)
      print(f"Sorry, that's wrong! Final Score = {score}")
      game_completed = True

  elif answer == "B":
    if data[i]['follower_count'] < data[i+1]['follower_count']:
      score += 1
      subprocess.run('clear', shell=True)
      print(logo)
      print(f"You're Right! Current Score = {score}")
      i += 1
    else:
      subprocess.run('clear', shell=True)
      print(logo)
      print(f"Sorry, that's wrong! Final Score = {score}")
      game_completed = True
