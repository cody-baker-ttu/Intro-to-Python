import random
moves = [ "Rock", "Paper", "Scissors"]
computer = random.choices( moves, k = 1)
user = input("Please enter Rock, Paper, or Scissors. ")
if user=="Rock" and computer=="Scissors":
        print("You Win!")
        else:
        print("You Lose!")
if user=="Scissors" and computer=="Paper":
        print("You Win!")
        else:
        print("You lose!")
if user=="Paper"  and computer=="Rock":
        print("You win!")
        else:
        print("You lose!")
