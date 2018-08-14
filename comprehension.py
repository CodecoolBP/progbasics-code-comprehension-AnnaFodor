# This program generates a number between 1 and 20 and lets the player take guesses in order to guess the number.

import random  # Provide access to generate random numbers

guesses_taken = 0  # Assign 0 to guesses_taken variable

print('Hello! What is your name?')  # Print strings between: ('') to console
myName = input()  # Assign the input of the user to myName

number = random.randint(1, 20)  # Assign random integer from 1 to 20 to number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
# Print the myName variable and strings (between '') to console

while guesses_taken < 6:  # The code will execute as long as guesses_taken < 6
    print('Take a guess.')  # Print strings between: ('') to console
    guess = input()  # Assign the input of the user to guess variable
    guess = int(guess)  # Change guess variable to integer
    guesses_taken += 1  # Assign +1 to guesses_taken variable

    if guess < number:  # If this condition true: guess variable lower than number variable
        print('Your guess is too low.')  # Print strings between: ('') to console

    if guess > number:  # If this condition true: guess variable higher than number variable
        print('Your guess is too high.')  # Print strings between: ('') to console

    if guess == number:  # If this condition true: guess variable equals number variable
        break  # It terminates the while loop

if guess == number:  # If this condition true: guess variable equals number variable
    guesses_taken = str(guesses_taken)  # Change guesses_taken to string
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')
# Print the myName, guesses_taken variable and strings (between '') to console

if guess != number:  # If this condition true: guess variable not equals number variable
    number = str(number)  # Change number to string
    print('Nope. The number I was thinking of was ' + number)
# Print number variable and strings (between '') to console
