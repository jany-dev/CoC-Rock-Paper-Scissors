#import modeules


#options for the game
import random
options = ["Rock", "Paper", "Scissors"]

computer = random.choice(options)
    #start the game
print("Welcome to Rock Paper Scissors!")
player = input("Type in your choice:")


print("Computer says: " + computer)

#logic of the game
if player == computer:
    print ("Draw") 
elif player == "Rock" and computer == "Paper":
    print("Paper wins!")
elif player == "Paper" and computer  == "Rock":
    print("Paper wins!")
elif player == "Scissors" and computer == "Rock":
    print("Rock wins!")
elif player == "Rock" and computer == "Scissors" :
    print("Rock wins!")
elif player == "Paper" and computer == "Scissors" :
    print("Scissors wins!")
elif player == "Scissors" and computer == "Paper" :
    print("Scissors wins!")
