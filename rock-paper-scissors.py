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
game_images=[rock, paper, scissors]

#user input selection and print
user=input("Please select one of the options: 1 for Rock, 2 for Paper and 3 for Scrissors\n")

if int(user) >3:
  print("Invalid Input. You Lose!")
else:
  print("You played\n")
  print(game_images[int(user)-1]) 

  #Computer random selection and print
  print("Computer played\n")
  comp=str(random.randint(1,3))
  print(game_images[int(comp)-1])

  #Who wins or lose
  if user==comp:
    print("Both players played the same hand.Please Go Again")
  elif user=="1" and comp=="3":
    print("You Win!")
  elif user=="2" and comp=="1":
    print("You Win!")
  elif user=="3" and comp=="2":
    print("You Win!")
  else:
    print("You Lose!")




