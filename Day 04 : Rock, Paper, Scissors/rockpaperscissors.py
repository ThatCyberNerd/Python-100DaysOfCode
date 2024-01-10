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

choice = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors : ")
print("-------------------------------------------")
print("You Chose :")

if choice == "0":
  print(rock)
elif choice == "1":
  print(paper)
elif choice == "2":
  print(scissors)
else:
  print("Invalid Choice!")

print("Computer Chose :")

computer = random.randint(0,2)

if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
elif computer == 2:
  print(scissors)

if choice == "0" and computer == 2:
   print("You Won!")
elif computer == 0 and choice == "2":
   print("You Lost!")
elif computer > int(choice):
   print("You Lost!")
elif computer == int(choice):
   print("It's a tie!")
else:
   print("You Won!")
