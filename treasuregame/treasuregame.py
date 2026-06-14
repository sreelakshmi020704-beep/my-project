print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to treasure island")
print(" your mission is to find treasure")
choice1 = input('you are at crossroad, where you want go? Type "left" or "right".').lower()
if choice1 == "left":
    choice2 = input('you\'ve come to a lake.\n'
          'There is an island in the middle of the lake.\n' 
          'Type "wait" to wait for a boat.\n'
          'type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input('you\'ve arrive at the island unharmed.\n'
              'There is a house with 3 door.\n'
              'One Red One Blue, One Yellow.\n'
              'Which colour do you choose?\n').lower()
        if choice3 == "red":
            print("it's room full of fire. Gameover.")
        elif choice3 == "yellow":
            print("You found the treasure. you win")
        elif choice3 == "blue":
            print("the room is full of beast. Gameover.")
        else:
            print("you choose the door that does'nt exist. Gameover.")   
    if choice2 == "swim":
        choice4 = input('you saw a boat.\n'
                        'Do you want to take it?\n'
                        'if you want to take it Type "yes"\n'
                        'if you don\'t wanna take it Type "no"')
        if choice4 == "yes":
            choice5 = input('you\'ve arrive at the island unharmed.\n'
              'There is a house with 3 door.\n'
              'One Red One Blue, One Yellow.\n'
              'Which colour do you choose?\n').lower()
            if choice5 == "red":
                print("it's room full of fire. Gameover.")
            elif choice5 == "yellow":
                print("You found the treasure. you win")
            elif choice5 == "blue":
                print("the room is full of beast. Gameover.")
            else:
                print("you choose the door that does'nt exist. Gameover.")
        elif choice4 == "no":
            print("you are out of breath and died. Gameover")
        else:
            print("wrong input")
                         
else:
    print("you fell in to a hole. Gameover")