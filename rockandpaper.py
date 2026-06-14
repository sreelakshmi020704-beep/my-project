import random
# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = '''     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock,paper,scissors]

user_choice = int(input("what do you wanna choose? type 0 for rock , 1 for paper, 2 for scissors"))

if user_choice >= 0 and user_choice <= 2:
    print(game_image[user_choice])
    
computer_choice = random.randint(0,2) 
print("computer chose")
print(game_image[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("you typed invalid number.you lose")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print("you lose")
    
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you won")
elif computer_choice == user_choice:
    print("its a draw")
else:
    print("invalid number. you lose")