#First, I will start by having the computer import the random module from Python
import random
#Now, I will initialize the numbers from which the computer can choose
length=100
#The line variable above sets the length for the array of numbers to 100
num=[None]*length
#this builds an array of zeros of length 100
for i in range(1, length+1):
        num[i-1] = i;
#this replaces the array of zeros with an array going from 1 to 100
#Now, I need for the computer to select a random number between 1 and 100
choice=random.choices(num, k = 1)
#this command creates a variable called choice which selects a random number from 1 to 100

#Now, I need to ask for user input so that I can compare user input to the variable choice.
guess=input("Choose a number from 1 to 100: ")
#the variable above asks the user to enter a number between 1 and 100

##Now, I need to set up an if statement to tell the user whether or not they got the guess correct,$

if guess==choice:
        print("Correct! You win on the first try!")
else:
        guess=input("Incorrect! Try again! Enter another number between 1 and 100. ")

#Now, I will give the user another chance to guess the correct number

if guess==choice:
        print("Correct! You win on the second try!")
else
        print("Incorrect! You lose the game!")
