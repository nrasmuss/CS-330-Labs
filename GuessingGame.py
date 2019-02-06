# This program was written by Nicole Rasmussen
# This program is a guessing game.
import random

number_of_guesses = 0
correct = False
number = random.randint(1,10)
guesses = ""
print(number)
name = input("What is your name? ")
while(correct == False and number_of_guesses < 7):
    guess = int(input("Please guess a number between 1 and 10 "))
    if guess == number:
        correct = True
    number_of_guesses += 1
    guesses = guesses +  str(guess) + ", "
if correct == True:
    print(name + ", you won the guessing game!")
    print("It took you " + str(number_of_guesses) + " guesses to correctly guess " + str(number))
    print("Here are all your guesses: " + guesses)
else:
    print("You have used all your guesses. Here are all the numbers you guessed: ")
    print(guesses)
    print("The correct number was: " + str(number))
