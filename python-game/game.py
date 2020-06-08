import random

options = ["Rock","Paper","Scissors"]
computer = random.choice(options)
print("Welcome to Rock Paper Scissors!")
user = input("Type in your choice: ")
user = user.lower()

if user == 'rock':
    if computer == 'Rock':
        print ('Tie Game')
    elif computer == 'Paper':
        print ('Computer Wins')
    else:
        print ('User Wins')
if user == 'paper':
    if computer == 'Rock':
        print ('User Wins')
    elif computer == 'Paper':
        print ('Tie Game')
    else:
        print ('Computer Wins')
if user == 'scissors':
    if computer == 'Rock':
        print ('Computer Wins')
    elif computer == 'Paper':
        print ('User Wins')
    else:
        print ('Tie Game')