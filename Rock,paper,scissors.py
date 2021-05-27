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

user_select = input("Choose a number: Rock = 0, Paper = 1 or Scissors = 2?\n")

if user_select == "0":
  print (rock)
elif user_select == "1":
  print (paper)
else:
  print (scissors)

computer_select = random.randint(0, 2)

print(f"computer chose {computer_select}")

if computer_select == 0:
  print (rock)
elif computer_select == 1:
  print (paper)
else:
  print (scissors)


if computer_select == 0 and user_select == "2":
  print ("computer wins")
elif computer_select == 2 and user_select == "1":
  print ("computer wins")
elif computer_select == 1 and user_select == "0":
  print ("computer wins")
elif computer_select == 0 and user_select == "0":
  print ("draw")
elif computer_select == 1 and user_select == "1":
  print ("draw")
elif computer_select == 2 and user_select == "2":
  print ("draw")
else:
  print ("user wins!")