# Welcome to the Number Guessing Game!
# I'm thinking of a number between 1 and 100.
# Choose a difficulty. Type 'easy' or 'hard':
import random

print("Welcome to the Number Guessing Game!\n"
"I'm thinking of a number between 1 and 100.\n"
"Choose a difficulty. Type 'easy' or 'hard':")
computer_choice=random.randint(1,100)
difficulty_level=input()
if difficulty_level not in ('easy','hard'):
    print("Choose the difficulty level only between hard or easy to start the game.")
elif difficulty_level=="hard":
    no_of_attempts_when_hard=5
    for i in range(1,6):
        print(f"You have {no_of_attempts_when_hard} attempts remaining to guess the number.\n""Make a guess:")
        number_choose=int(input())
        if number_choose == computer_choice:
            print("You won")
            break
        elif number_choose < computer_choice:
            print("too low")
        elif number_choose > computer_choice:
            print("too high")
        no_of_attempts_when_hard-=1
    print(f"the guessed number by computer was {computer_choice}")
elif difficulty_level=="easy":
    no_of_attempts_when_easy=10
    for i in range(1, 11):
        print(f"You have {no_of_attempts_when_easy} attempts remaining to guess the number.\n""Make a guess:")
        number_choose = int(input())
        if number_choose == computer_choice:
            print("You won")
            break
        elif number_choose < computer_choice:
            print("too low")
        elif number_choose > computer_choice:
            print("too high")
        no_of_attempts_when_easy -= 1
    print(f"the guessed number by computer was {computer_choice}")

