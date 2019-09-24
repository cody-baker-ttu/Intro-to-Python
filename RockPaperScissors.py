import random
moves = [ "Rock", "Paper", "Scissors"]
computer = random.choices( moves, k = 1)
user = input("Please enter Rock, Paper, or Scissors. ")
if(user=="Rock" and computer=="Scissors"):
        print("You win!")
elif(user=="Scissors" and computer=="Paper"):
        print("You Win!")
elif(user=="Paper" and computer=="Rock"):
        print("You win!")
elif(user=="Paper" and computer=="Scissors")
        print("You lose.")
elif(user=="Rock" and computer=="Paper")
        print("You lose.")
elif(user=="Scissors" and computer=="Rock")
        print("You lose.")
else:
        print("There is a tie.")
