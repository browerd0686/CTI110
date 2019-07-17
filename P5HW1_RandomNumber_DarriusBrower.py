# Random Number Excercise
# July 16, 2019
# CTI-110 P5HW1- Random Number
# Darrius Brower
#
# Write a program that generates a random number in the range of 1 to 100.
# Ask the user to guess what the number is.
# The program should tell the user if their guess is too high or too low and try again.
# If the user guesses the number, the program should congratulate them and generate a new number.
#
import random

def generateRandomNumber():
    randomNumber = random.randint(1,100)
    return randomNumber

def askUserForNumber(message = 'Guess the number: '):
    userNumber = int(input(message))
    return userNumber

def checkUserNumber(userNumber, randomNumber):
    if userNumber > randomNumber:
        return 'Too high'
    elif userNumber < randomNumber:
        return 'Too low'
    else:
        return 'Congratulations!'

def main():
    userCongratulated = False
    letsStart = True

    while userCongratulated or letsStart:
         randomNumber = generateRandomNumber()
         #print('For testing purposes, random number: ', randomNumber)
         userNumber = askUserForNumber()
         message = checkUserNumber(userNumber, randomNumber)

         while message != 'Congratulations!':
             print(message)
             userNumber = askUserForNumber('Try again:')
             message = checkUserNumber(userNumber, randomNumber)

         print(message)
         userCongratulated = True

main()
         
    
