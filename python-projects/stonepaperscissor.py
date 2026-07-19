#This program is to play stone,papaer and scissor game with computer.

print("Welcome!\nLet's start the game.....")
import random
list=["stone","paper","scissor"]
computer_choice=random.choice(list)
you_wanna_play="yes"
while(you_wanna_play=="yes"):
    user_choice = input("Choose among stone, paper and scissor:\n")
    user_choice.lower()
    if user_choice not in ("stone", "paper", "scissor"):
        print("You only have to choose among among stone, paper and scissor to play the game")
        you_wanna_play = input("Do you wanna play again- yes or no?\n")
        continue
    elif user_choice=="paper" and computer_choice=="stone":
        print("Hurray you won")
    elif user_choice=="stone" and computer_choice=="scissor":
        print("Hurray you won")
    elif user_choice=="scissor" and computer_choice=="paper":
        print("Hurray you won")
    elif user_choice=="scissor" and computer_choice=="scissor":
        print("the game is draw")
    elif user_choice=="stone" and computer_choice=="stone":
        print("the game is draw")
    elif user_choice=="paper" and computer_choice=="paper":
        print("the game is draw")
    elif user_choice=="stone" and computer_choice=="scissor":
        print("Oops you loose")
    elif user_choice=="stone" and computer_choice=="paper":
        print("Oops you loose")
    elif user_choice=="paper" and computer_choice=="scissor":
        print("Oops you loose")
    print(f"The computer choosen {computer_choice}")
    you_wanna_play=input("Do you wanna play again- yes or no?\n")
    you_wanna_play.lower()

