from art import highlow
from art import vs
from gamedata import data
import random


def format_data(account):
    """Formats the account data into printable format."""
    account_name = account['name']
    accounnt_description = account['description']
    account_country = account['country']
    return f"Compare A: {account_name}, a {accounnt_description}, from {account_country}."

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"    
    

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:  
    print(highlow)
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n"*20)

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1
        print(f"you are right! current score: {score}")
    else:
        print(f"you are wrong! current score: {score}")
        game_should_continue = False
        
        