import random
from random import randint
import time
import os


#For clearing the terminal
if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()

#Game instructions
print("This game is for entertainment purposes.")
time.sleep(1)
print("The game Instructions are as follows:-")
time.sleep(1)
print("There are two dices in this game.")
time.sleep(3)
print("When the dices are rolled the coming numbers will be displayed.")
time.sleep(3)
print("And if the total of the numbers coming on the dices is 12 then you will win the game.")
time.sleep(3)
print("If the total is other than 12, the game will continue.")
time.sleep(3)
print("To end the game please enter 'no' when asked to roll again.")
time.sleep(3)
print("I hope you understood the Instructions.")
time.sleep(2)
print("So Without wasting any time Let's begin the game...:)")
time.sleep(2)
start = input("For starting the game enter 'yes': ")
time.sleep(1)


#if conditions for starting the game 
if start == "no":
    print("Ok no problem..You can play later whenever you want!")
    time.sleep(2)
    print("Till then Good bye :(")
    exit()
    
elif start != "yes":
    print("Sorry Invalid input...\nCannot start the game..:(")
    print("Please try again....")
    time.sleep(2)
    exit()

#While loop for playing the game endlessly until the desired output is achieved
repeat = True
while repeat:
    time.sleep(1)
    
    die1 = randint(1,6)         #Die1 output 
    die2 = randint(1,6)         #Die2 output
    
    total = die1 + die2         #For the total of numbers of die1 and die2
    
    print("Dice rolled as {} and {}".format(die1,die2))         #Printing statement for numbers coming in dices
    
    print("The total is {}".format(total))                      #Printing statement for  the total of numbers coming in the dices
    
    if total == 12:                                     #if condition for ending the while loop
        time.sleep(1)
        print("You won!\nCongractulations.....")
        time.sleep(2)
        print("You can play again If you want  :) or maybe later :(")
        time.sleep(3)
        print("Till then Thanks for playing....:)")
        exit()

    repeat = input("\nTo roll again enter 'yes' or 'y': ").lower()          #Repeating statement for repeating the game until the output is achieved

    if repeat == "no":                                                  #if conditions for ending the repeat statement
        print("OK no problem you can play whenever you want later....")
        time.sleep(2)
        print("Till then Thanks for playing....:)")
        exit()

    elif repeat!= "y":
        print("Invalid input! Please try again...")
        exit()