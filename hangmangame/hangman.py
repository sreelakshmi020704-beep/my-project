import random
from hangman_words import word_list
from hangman_art import stages,logo



lives = 6

print(logo)
 
choosed = random.choice(word_list)

placeholder = "_"
choosdedlen = len(choosed)

for postion in range(choosdedlen):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []

while not game_over:
    
    print(f"**************{lives}/6 lives left**************")
    guess = input("Word to guess").lower()
    
    
    if guess in correct_letter:
        print(f"you've already guessed {guess}")
    
    display = ""


    for letter in choosed:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
            
    print(display)
    
    if guess not in choosed:
        lives -= 1
        print(f"you guessed {guess}, that's not in the word. You lose a life.")
        
        if lives == 0:
            game_over = True
            print("**************YOU LOSE**************")
    
    if "_" not in display:
        game_over = True
        print("**************YOU WIN**************")
    
    print(stages[lives])
print("the word is")
print(choosed)