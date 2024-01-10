logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

import sys, subprocess

print(logo)
print("Welcome To The Secret Auction!")

bidders = {}
bidding_done = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_done:
  name = input("Enter your name : ")
  bid = int(input("How much do you wanna bid? $"))  
  bidders[name] = bid
  continuation = input("Are there any other bidders? Type 'yes' or 'no'")
  if continuation == "no":
    bidding_done = True
    find_highest_bidder(bidders)
  else:
    subprocess.run('clear', shell=True)
